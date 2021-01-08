import torch.nn as nn 
from torchvision import models
import torch.optim as optim
import torch
from dictionary import Vocabulary,EOS_token,PAD_token,SOS_token,UNK_token 
from torch.nn import functional as F


if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

# Encoder VGG19 as base model
class Encoder(nn.Module):
    
    def __init__(self,batch_size):
        super(Encoder,self).__init__()
        base_model = models.vgg19(pretrained=True)
        layers_to_use = list(base_model.features.children())[:29]
        self.model = nn.Sequential(*layers_to_use)
        
    def forward(self,image_batch):
        batch_size = image_batch.size()[0]
        output = self.model(image_batch).view(batch_size,512,-1)
        output = output.permute(0,2,1)
        return output

# Attention Model
class SpatialAttention(nn.Module):
    def __init__(self,hidden_size, feat_size, bottleneck_size):
        super(SpatialAttention,self).__init__()
        '''
        Spatial Attention module. It depends on previous hidden memory in the decoder(of shape hidden_size),
        feature at the source side ( of shape(196,feat_size) ).  
        at(s) = align(ht,hs)
              = exp(score(ht,hs)) / Sum(exp(score(ht,hs')))  
        where
        score(ht,hs) = ht.t * hs                         (dot)
                     = ht.t * Wa * hs                  (general)
                     = va.t * tanh(Wa[ht;hs])           (concat)  
        Here we have used concat formulae.
        Argumets:
          hidden_size : hidden memory size of decoder.
          feat_size : feature size of each grid (annotation vector) at encoder side.
          bottleneck_size : intermediate size.
        '''
        self.hidden_size = hidden_size
        self.feat_size = feat_size
        self.bottleneck_size = bottleneck_size
        
        self.decoder_projection = nn.Linear(hidden_size,bottleneck_size)
        self.encoder_projection = nn.Linear(feat_size, bottleneck_size)
        self.final_projection = nn.Linear(bottleneck_size,1)
     
    def forward(self,hidden,feats):
        '''
        shape of hidden (hidden_size)
        shape of feats (196,feat_size)
        '''
        Wh = self.decoder_projection(hidden)  # (256)
        Uv = self.encoder_projection(feats)   # (60,256)
        #print(' Wh(hidden to bottleneck)  Uv(Feats to bottleneck)',Wh.size(),Uv.size())
        Wh = Wh.unsqueeze(1).expand_as(Uv)
        #print('Wh size  : ',Wh.size())
        energies = self.final_projection(torch.tanh(Wh+Uv))
        #print('energies : ',Uv.size())
        weights = F.softmax(energies, dim=1)
        
        weighted_feats = feats *weights.expand_as(feats)
        attn_feats = weighted_feats.sum(dim=1)
        return attn_feats,weights



# Decoder with attention
class Decoder(nn.Module):
    
    def __init__(self, feat_size, feat_len, embedding_size, hidden_size, attn_size, output_size, rnn_dropout,
                num_layers = 1, num_directions = 1):
        super(Decoder, self).__init__()
        '''
        Decoder, Basically a language model.
        
        Arguments:
        hidden_size : hidden memory size of LSTM/GRU
        output_size : output size. Its same as the vocabulary size.
        n_layers : 
        
        '''

        # Keep for reference
        self.feat_size = feat_size
        self.feat_len = feat_len
        self.embedding_size = embedding_size
        self.hidden_size = hidden_size
        self.attn_size = attn_size
        self.output_size = output_size
        self.rnn_dropout = rnn_dropout
        
        self.num_layers = num_layers
        self.num_directions = num_directions

        # Define layers
        self.embedding = nn.Embedding(self.output_size, self.embedding_size)
        
        self.attention = SpatialAttention(hidden_size = self.num_directions*self.hidden_size,
                                          feat_size=self.feat_size,
                                          bottleneck_size=self.attn_size)
        
        
        self.rnn = nn.LSTM(self.embedding_size+self.feat_size, self.hidden_size,
                           self.num_layers, dropout=self.rnn_dropout,batch_first=False, 
                          bidirectional=True if self.num_directions ==2 else False)
        
        self.out = nn.Linear(self.num_directions*self.hidden_size, self.output_size)

    def get_last_hidden(self, hidden):
        
        last_hidden = hidden[0] if isinstance(hidden,tuple) else hidden
        last_hidden = last_hidden.view(self.num_layers, self.num_directions,
                                       last_hidden.size(1),last_hidden.size(2))
        last_hidden = last_hidden.transpose(2,1).contiguous()
        last_hidden = last_hidden.view(self.num_layers,last_hidden.size(1),
                                       self.num_directions*last_hidden.size(3))
        last_hidden = last_hidden[-1]
        return last_hidden
    
    
    def forward(self, inputs, hidden, feats):
        # Note: we run this one step (word) at a time
        # Get embedding of current input word
        
        # inputs -  (1,batch)
        # hidden - (num_layers * num_directions, batch, hidden_size)
        # feats - (batch,attention_length,annotation_vector_size) (32,196,512)
        
        #print('input  hidden  feats :',inputs.size(),hidden[0].size(),feats.size())
        
        embedded = self.embedding(inputs)
        
        last_hidden = hidden[0]
        #print('embedded size :',embedded.size())
        
        feats, attn_weights = self.attention(last_hidden.squeeze(0),feats)

        input_combined = torch.cat((embedded,feats.unsqueeze(0)),dim=2)
        #print('input combined :',input_combined.size())

        output, hidden = self.rnn(input_combined, hidden)

        output = output.squeeze(0)
        output = self.out(output)
        output = F.softmax(output, dim = 1)
        
        return output, hidden, attn_weights


# Show Attend and Tell model
class ShowAttendTell(nn.Module):
    
    def __init__(self,encoder,decoder,vocabulary,teacher_forcing_ratio, batch_size):#=batch_size,):
        super(ShowAttendTell,self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.voc = vocabulary
        self.batch_size = batch_size
        self.enc_optimizer = optim.Adam(self.encoder.parameters(),lr=0.00001)
        self.dec_optimizer = optim.Adam(self.decoder.parameters(),lr=0.001)
        self.teacher_forcing_ratio = teacher_forcing_ratio
        self.print_every = 400
        
    def update_hyperparam(self,encoder_lr,decoder_lr,teacher_forcing_ratio):
        self.encoder_lr = encoder_lr
        self.decoder_lr = decoder_lr
        self.enc_optimizer = optim.Adam(self.encoder.parameters(),lr=self.encoder_lr)
        self.dec_optimizer = optim.Adam(self.decoder.parameters(),lr=self.decoder_lr)
        self.teacher_forcing_ratio = teacher_forcing_ratio
 
        
    def load(self,encoder_path = 'Save/VGG_encoder_10.pt',decoder_path='Save/VGG_decoder_10.pt'):
        self.encoder = torch.load(encoder_path)
        self.decoder = torch.load(decoder_path)
        #self.encoder.load_state_dict(torch.load(encoder_path))
        #self.decoder.load_state_dict(torch.load(decoder_path))
        
    def train_epoch(self,dataloader,clip=5):
        
        total_loss = 0
        start_iteration = 1
        print_loss = 0
        iteration = 1
        for data in dataloader:
            features, targets, mask, max_length,_ = data
            use_teacher_forcing = True if random.random() < self.teacher_forcing_ratio else False
            loss = self.train_iter(features,targets,mask,max_length,use_teacher_forcing,clip)
            print_loss += loss
            total_loss += loss

        # Print progress
            if iteration % self.print_every == 0:
                print_loss_avg = print_loss / self.print_every
                print("Iteration: {}; Percent complete: {:.1f}%; Average loss: {:.4f}".
                format(iteration, iteration / len(dataloader) * 100, print_loss_avg))
                print_loss = 0
            
            iteration += 1
            
        return total_loss/len(dataloader)
            
        
    def train_iter(self,input_variable, target_variable, mask,max_target_len,use_teacher_forcing,clip=5):
        
        self.enc_optimizer.zero_grad()
        self.dec_optimizer.zero_grad()
        
        loss = 0
        print_losses = []
        n_totals = 0
        
        input_variable = input_variable.to(device)
        target_variable = target_variable.to(device)
        mask = mask.byte().to(device)
        
        enc_output = self.encoder(input_variable)
        decoder_input = torch.LongTensor([[SOS_token for _ in range(batch_size)]])
        decoder_input = decoder_input.to(device)
        decoder_hidden = (torch.zeros(1, batch_size, self.decoder.hidden_size).to(device),
                  torch.zeros(1, batch_size, self.decoder.hidden_size).to(device))
        
        # Forward batch of sequences through decoder one time step at a time
        if use_teacher_forcing:
            for t in range(max_target_len):
                decoder_output, decoder_hidden,_ = self.decoder(decoder_input, decoder_hidden,enc_output)
                decoder_input = target_variable[t].view(1, -1)
                mask_loss, nTotal = maskNLLLoss(decoder_output.unsqueeze(0), target_variable[t], mask[t])
                loss += mask_loss
                print_losses.append(mask_loss.item() * nTotal)
                n_totals += nTotal
        else:
            for t in range(max_target_len):
                #print('decoder hidden in sampling :',decoder_hidden.size())
                decoder_output, decoder_hidden,_ = self.decoder(decoder_input, decoder_hidden,enc_output )
                # No teacher forcing: next input is decoder's own current output
                _, topi = decoder_output.squeeze(0).topk(1)
                decoder_input = torch.LongTensor([[topi[i][0] for i in range(self.batch_size)]])
                decoder_input = decoder_input.to(device)
                #print('decoder input size in training :',decoder_input.size())
                # Calculate and accumulate loss
                mask_loss, nTotal = maskNLLLoss(decoder_output, target_variable[t], mask[t])
                loss += mask_loss
                print_losses.append(mask_loss.item() * nTotal)
                n_totals += nTotal

        # Perform backpropatation
        loss.backward()

        # Clip gradients: gradients are modified in place
        _ = nn.utils.clip_grad_norm_(self.encoder.parameters(), clip)
        _ = nn.utils.clip_grad_norm_(self.decoder.parameters(), clip)

        # Adjust model weights
        self.enc_optimizer.step()
        self.dec_optimizer.step()

        return sum(print_losses) / n_totals
            
        
    def Greedy_Decoding(self,features,max_length=15):
        enc_output = self.encoder(features)
        batch_size = features.size()[0]
        decoder_hidden = (torch.zeros(1, batch_size, self.decoder.hidden_size).to(device),
                          torch.zeros(1, batch_size, self.decoder.hidden_size).to(device))
        
        decoder_input = torch.LongTensor([[SOS_token for _ in range(batch_size)]]).to(device)
        #print('Initial size',decoder_input.size())
        caption = []
        attn_weights = []
        for _ in range(max_length):
            decoder_output, decoder_hidden, attn_values = self.decoder(decoder_input, decoder_hidden, enc_output)
            #print(attn_values.shape)

            #print('decoder hidden size :',decoder_hidden.size())
            #print('decoder output size :',decoder_output.size())
            _, topi = decoder_output.topk(1)
            #print(topi)
            #print('topi size',topi.size())
            decoder_input = topi.permute(1,0).to(device)
            caption.append(topi.squeeze(1).cpu())
            attn_weights.append(attn_values[:,:,0].cpu())
        caption = torch.stack(caption,0).permute(1,0)
        attn_weights= torch.stack(attn_weights,0)
        #print(attn_weights.size())

        caps_text = []
        for dta in caption:
            tmp = []
            for token in dta:
                if token.item() not in self.voc.index2word.keys() or token.item()==2:
                    pass
                else:
                    tmp.append(self.voc.index2word[token.item()])
            tmp = ' '.join(x for x in tmp)
            caps_text.append(tmp)
        return caption,caps_text,attn_weights
    


