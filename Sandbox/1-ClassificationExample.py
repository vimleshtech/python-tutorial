import pandas as pd  
import os
import sklearn as sk  
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

os.chdir('C:/Users/vkumar15/Desktop/Learning & Training/Weekend/Sunday')  
heart = pd.read_csv('Heart.csv')   #, sep=',', header=0
print(heart.head())

heart = heart.drop(columns=['row.names'])
print(heart.head())


y = heart.iloc[:,9]   #boolean  value on y 
x = heart.iloc[:,:4]   #rest all value on x

#print(y)
#print(x)

LR = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr').fit(x, y)  
o = LR.predict(x.iloc[460:,:])
print(o)
print(round(LR.score(x,y), 4))

#SVM
SVM = svm.LinearSVC()  
SVM.fit(x, y)  
SVM.predict(x.iloc[460:,:])  
print(round(SVM.score(x,y), 4))


#RF
RF = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)  
RF.fit(x, y)  
RF.predict(x.iloc[460:,:])  
print(round(RF.score(x,y), 4))


#
NN = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)  
NN.fit(x, y)  
NN.predict(x.iloc[460:,:])  
print(round(NN.score(x,y), 4))







