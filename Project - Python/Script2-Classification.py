import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set()

rating = pd.read_csv('hotels_travel_list.csv')
ax =sns.countplot(x="Rating", data=rating)
plt.show()

rating = pd.read_csv('restaurants_list.csv')
ax =sns.countplot(x="Rating", data=rating)
plt.show()



# Python script for confusion matrix creation. 
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report

#category  A to  category B
ratingA= pd.read_csv('hotels_travel_list.csv')
ratingB = pd.read_csv('hotels_travel_list.csv')

rateA =ratingA.values
rateB =ratingB.values

x = rateA[:,4].tolist()
y = rateB[:,4].tolist()

actual = x
predicted = y

results = confusion_matrix(actual, predicted) 
print ('Confusion Matrix :')
print(results) 
print ('Accuracy Score :',accuracy_score(actual, predicted) )
print ('Report : ')
print (classification_report(actual, predicted)) 

#category B to A

rateA =ratingA.values
rateB =ratingB.values

x = rateB[:,4].tolist()
y = rateA[:,4].tolist()

actual = x
predicted = y

results = confusion_matrix(actual, predicted) 
print ('Confusion Matrix :')
print(results) 
print ('Accuracy Score :',accuracy_score(actual, predicted) )
print ('Report : ')
print (classification_report(actual, predicted)) 





