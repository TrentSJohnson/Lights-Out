# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 23:39:02 2019

@author: trent
"""

import math

import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    input_dim = (40,40)
    def __init__(self,kernel1 = 5, kernel2 = 5, pooling = 2):
        super(Net, self).__init__()
        # 1 input image channel, 6 output channels, 5x5 square convolution
        # kernel
        self.pooling = pooling
        self.k1 = kernel1
        self.k2 = kernel2
        self.conv1 = nn.Conv2d(1,6, self.k1)
        self.conv2 = nn.Conv2d(6, 16, self.k2)
        w_reduct1 = math.floor((Net.input_dim[0] - self.k1 + 1)/2)
        self.output_width = math.floor((w_reduct1 - self.k2 + 1)/2)
        h_reduct1 = math.floor((Net.input_dim[1] - self.k1 + 1)/2)
        self.output_height = math.floor((h_reduct1 - self.k2 + 1)/2)

        #set affine operation to be y = wx + b
        self.fc1 = nn.Linear(16 * self.output_height * self.output_width, 120)
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,10)
        
    def forward(self,x):
        #Max pooling over (2,2)
        x = F.max_pool2d(F.relu(self.conv1(x)),self.pooling)
        x = F.max_pool2d(F.relu(self.conv2(x)),self.pooling)
        print(self.num_flat_features(x),16*5*5)
        x = x.view(-1,self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
        
    def num_flat_features(self,x):
        size = x.size()[1:] ##all dimensoins but batch
        num_features = 1
        for s in size:
            num_features *= s
        return num_features
        
net = Net()
params = list(net.parameters())

input = torch.randn(1, 1, 40, 40)
output = net(input)

target = torch.randn(10)
target = target.view(1,-1)
criterion = nn.MSELoss()

loss = criterion(output,target)

net.zero_grad()     # zeroes the gradient buffers of all parameters

loss.backward()
print(torch.randn(1,1,40,40))

