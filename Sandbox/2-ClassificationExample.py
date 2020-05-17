import pandas as pd  
import sklearn as sk  
from sklearn.linear_model import LogisticRegression  
from sklearn import svm  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.neural_network import MLPClassifier
import os

os.chdir('C:/Users/vkumar15/Desktop/Learning & Training/Weekend/Sunday')  
vowel_train = pd.read_csv('vowel.train.csv', sep=',',header=0)  
vowel_test = pd.read_csv('vowel.test.csv', sep=',',header=0)

vowel_train = vowel_train.drop(columns=['row.names'])
vowel_test = vowel_test.drop(columns=['row.names'])

y_tr = vowel_train.iloc[:,0]  
X_tr = vowel_train.iloc[:,1:]

y_test = vowel_test.iloc[:,0]  
X_test = vowel_test.iloc[:,1:]

LR = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(X_tr, y_tr)  
LR.predict(X_test)  
print(round(LR.score(X_test,y_test), 4))

SVM = svm.SVC(decision_function_shape="ovo").fit(X_tr, y_tr)  
SVM.predict(X_test)  
print(round(SVM.score(X_test, y_test), 4))

RF = RandomForestClassifier(n_estimators=1000, max_depth=10, random_state=0).fit(X_tr, y_tr)  
RF.predict(X_test)  
print(round(RF.score(X_test, y_test), 4))

NN = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(150, 10), random_state=1).fit(X_tr, y_tr)  
NN.predict(X_test)  
print(round(NN.score(X_test, y_test), 4)  )



