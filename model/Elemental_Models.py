class Focus_linear(nn.Module):
    '''
       linear focus network for elemental data
       inputs: number of input nodes
       output: number of output nodes
       returns linear layer output(for focus network a scalar)
    '''
    def __init__(self,inputs,output):
        super(Focus_linear,self).__init__()
        self.inputs = inputs
        self.output = output
        self.linear1 = nn.Linear(self.inputs,self.output)
    def forward(self,z):
        batch = z.shape[0]
        x = torch.zeros([batch,3],dtype=torch.float64)
        y = torch.zeros([batch,2], dtype=torch.float64)
        #x,y = x.to("cuda"),y.to("cuda")
        for i in range(3):
            x[:,i] = self.helper(z[:,2*i:2*i+2])[:,0]
        x = F.softmax(x,dim=1)   # alphas
        x1 = x[:,0]
        for i in range(3):
            x1 = x[:,i]          
            y = y+torch.mul(x1[:,None],z[:,2*i:2*i+2])
        return y , x 
    def helper(self,x):
        x = self.linear1(x)
        return x

class Classification_linear(nn.Module):
    '''
    linear classification network
    inputs: number of input nodes
    output: number of output nodes
    returns linear layer output for classification
    
    '''
    def __init__(self,inputs,output):
        super(Classification_linear,self).__init__()
        self.inputs= inputs
        self.output = output
        self.linear1 = nn.Linear(self.inputs,self.output)

    def forward(self,x):
        x = self.linear1(x)
        return x  

class Focus_deep(nn.Module):
    '''
       deep focus network averaged at zeroth layer
       inputs :  inputs: number of input nodes
       output: number of output nodes
       returns second layer output for focus (a scalar for focus network)
  
    '''
    def __init__(self,inputs,output):
        super(Focus_deep,self).__init__()
        self.inputs = inputs
        self.output = output
        self.linear1 = nn.Linear(self.inputs,50)  #,self.output)
        self.linear2 = nn.Linear(50,self.output) 
    def forward(self,z):
        batch = z.shape[0]
        x = torch.zeros([batch,3],dtype=torch.float64)
        y = torch.zeros([batch,2], dtype=torch.float64)
        #x,y = x.to("cuda"),y.to("cuda")
        for i in range(3):
            x[:,i] = self.helper(z[:,2*i:2*i+2])[:,0]
        x = F.softmax(x,dim=1)   # alphas
        x1 = x[:,0]
        for i in range(3):
            x1 = x[:,i]          
            y = y+torch.mul(x1[:,None],z[:,2*i:2*i+2])
        return y , x 
    def helper(self,x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        #x = self.linear3(x)
        return x

class Classification_deep(nn.Module):
    '''
       deep classification module data averaged at zeroth layer
       inputs: number of input nodes
       output: number of output nodes
       returns second layer output for classification
       
    '''
    def __init__(self,inputs,output):
        super(Classification_deep,self).__init__()
        self.inputs = inputs
        self.output = output
        self.linear1 = nn.Linear(self.inputs,50)
        self.linear2 = nn.Linear(50,self.output)


    def forward(self,x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x    