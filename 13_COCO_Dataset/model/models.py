import torch.nn as nn 
from torchvision import models

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