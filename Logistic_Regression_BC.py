import sklearn.datasets
import torch
import torch.nn as nn 
import sklearn 
import numpy as np
from sklearn.preprocessing import StandardScaler


'''

-- What needs to be done in the day: 

- Just complete this program 
- Watch and understand the 20 minute video on datasets and dataloaders (with notes)
- Implement what you just watched 
- Post it on X for now 

- In the weekend, also post on the LinkedIn of the progress that you have made
- Do not get up  until done please! 

but it will take time and that I do not have for now, how do I solve it? I think whenever I am feeling this way it is usually unfinished tasks that have been 
taking my mindspace, for most often, I need to make sure that there has been 

Implement Logistic Regression of the BC Dataset

Steps involved: 
- Dowload the Dataset X and y 
- Make sure to have the target 

- Define the Standarad Scaler for the Data

- Define the Logistic Regression Model, with the Softmax Activation Function.
 Define the optimizer 
- Define the loss 

- Define the learing rate 
Training Loop: 
    - Make the prediction: from model.predict method
    - Calculate the loss, using the loss function 
    - Backpropogation: Calculate the gradients of loss wrt to weights 
    - Update the weights (optim.step()) method 
    - Set the gradients to zero by optim.zero_grad() function 
    - Print the prediciction for the model
'''

## Deifining the dataset: 

X,y = sklearn.datasets.load_breast_cancer(return_X_y=True)
# print(X.shape, y.shape)

## Standard Scaler

sc = StandardScaler()
X_train = sc.fit_transform(X)

# Convert y to a PyTorch tensor and reshape
# y = torch.from_numpy(y).to(dtype=torch.float32)
# y_train = y.view((y.shape[0]))
# y_train = torch.reshape(y_train, (y_train.shape[0],1))
# print(X_train.shape, y_train.shape)

X_train_torch = torch.FloatTensor(X_train)
y_train = torch.FloatTensor(y).reshape(-1, 1)  # Changed to FloatTensor and reshape
print(X_train.shape, y_train.shape)

n_features = X_train.shape[1]
n_samples = X_train.shape[0]

## Model Definition: 

class Logistic_Regression(nn.Module): 
    def __init__(self,input_features): 
        super(Logistic_Regression,self).__init__()
        self.linear = nn.Linear(input_features,1)
    
    def forward(self,x): 
        y_pred = torch.sigmoid(self.linear(x))
        return y_pred

model  = Logistic_Regression(n_features)

## Loss and Optimizer: 
lr = 0.01 
loss_fn = nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(),lr=lr)


## Training Loop
n_epoch = 10000
X_train_torch = torch.from_numpy(X_train).to(dtype=torch.float32)

for epoch in range(n_epoch):
    '''
    What happens in the training loop? 
        - make the prediction 
        - Calculate the loss 
        - calculate loss.backwards 
        - optim.step for the weights update 
        - optim.zero_ something to make all the weights to 0
        - Print the prediction after some itteration
    ''' 
    y_pred = model(X_train_torch)
    # print(y_pred)
    # print(f'Y_Pred: {y_pred.shape} Y: {y.shape}')
    loss = loss_fn(y_pred,y_train)

    loss.backward()
    optimizer.step() 
    optimizer.zero_grad()

    if epoch%100==0: 
        print(f'Epoch {epoch}, Loss: {loss}')