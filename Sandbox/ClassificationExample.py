# Scikit-learn, the most popular machine learning tool for Python.
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns


fruits = pd.read_table('fruits.txt')
print(fruits.head())

#Each row of the dataset represents one piece of the fruit as represented by several features that are in the table’s columns.

#We have 59 pieces of fruits and 7 features in the dataset:

print(fruits.shape)

#We have four types of fruits in the dataset:
print(fruits['fruit_name'].unique())

#The data is pretty balanced except mandarin. We will just have to go with it.
print(fruits.groupby('fruit_name').size())


#sns.countplot(fruits['fruit_name'],label="Count")
#plt.show()     

#Box plot for each numeric variable will give us a clearer idea of the distribution of the input variables:
#fruits.drop('fruit_label', axis=1).plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False, figsize=(9,9),                                         title='Box Plot for each input variable')
#plt.savefig('fruits_box')
#plt.show()


#It looks like perhaps color score has a near Gaussian distribution.
import pylab as pl
fruits.drop('fruit_label' ,axis=1).hist(bins=30, figsize=(9,9))
pl.suptitle("Histogram for each numeric input variable")
#plt.savefig('fruits_hist')
#plt.show()




#Some pairs of attributes are correlated (mass and width). This suggests a high correlation and a predictable relationship.
from pandas.tools.plotting import scatter_matrix
from matplotlib import cm
feature_names = ['mass', 'width', 'height', 'color_score']
X = fruits[feature_names]
y = fruits['fruit_label']
#cmap = cm.get_cmap('gnuplot')
#scatter = pd.scatter_matrix(X, c = y, marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(9,9), cmap = cmap)
#plt.suptitle('Scatter-matrix for each input variable')
#plt.savefig('fruits_scatter_matrix')


####statistical summary
print(fruits.drop(['fruit_label','mass'],axis=1).describe())


#Create Training and Test Sets and Apply Scaling
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print(X_train)
print(X_test)


#####################
#Build Models
#####################
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
print('Accuracy of Logistic regression classifier on training set: {:.2f}'
     .format(logreg.score(X_train, y_train)))
print('Accuracy of Logistic regression classifier on test set: {:.2f}'
     .format(logreg.score(X_test, y_test)))

#Decision Tree
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier().fit(X_train, y_train)
print('Accuracy of Decision Tree classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of Decision Tree classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))

#K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print('Accuracy of K-NN classifier on training set: {:.2f}'
     .format(knn.score(X_train, y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'
     .format(knn.score(X_test, y_test)))


#Linear Discriminant Analysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis()
lda.fit(X_train, y_train)
print('Accuracy of LDA classifier on training set: {:.2f}'
     .format(lda.score(X_train, y_train)))
print('Accuracy of LDA classifier on test set: {:.2f}'
     .format(lda.score(X_test, y_test)))


#Gaussian Naive Bayes
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train, y_train)
print('Accuracy of GNB classifier on training set: {:.2f}'
     .format(gnb.score(X_train, y_train)))
print('Accuracy of GNB classifier on test set: {:.2f}'
     .format(gnb.score(X_test, y_test)))


#Support Vector Machine
from sklearn.svm import SVC
svm = SVC()
svm.fit(X_train, y_train)
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))



##The KNN algorithm was the most accurate model that we tried. The confusion matrix provides an indication of no error made on the test set. However, the test set was very small.

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
pred = knn.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))


#Plot the Decision Boundary of the k-NN Classifier
##################
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.patches as mpatches
import matplotlib.patches as mpatches
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
X = fruits[['mass', 'width', 'height', 'color_score']]
y = fruits['fruit_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

def plot_fruit_knn(X, y, n_neighbors, weights):
     X_mat = X[['height', 'width']].as_matrix()
     y_mat = y.as_matrix()
     # Create color maps
     cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF','#AFAFAF'])
     cmap_bold  = ListedColormap(['#FF0000', '#00FF00', '#0000FF','#AFAFAF'])
     clf = KNeighborsClassifier(n_neighbors, weights=weights)
     clf.fit(X_mat, y_mat)
     # Plot the decision boundary by assigning a color in the color map
     # to each mesh point.
    
     mesh_step_size = .01  # step size in the mesh
     plot_symbol_size = 50
    
     x_min, x_max = X_mat[:, 0].min() - 1, X_mat[:, 0].max() + 1
     y_min, y_max = X_mat[:, 1].min() - 1, X_mat[:, 1].max() + 1
     xx, yy = np.meshgrid(np.arange(x_min, x_max, mesh_step_size),
                         np.arange(y_min, y_max, mesh_step_size))
     Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
     # Put the result into a color plot
     Z = Z.reshape(xx.shape)
     plt.figure()
     plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
     # Plot training points
     plt.scatter(X_mat[:, 0], X_mat[:, 1], s=plot_symbol_size, c=y, cmap=cmap_bold, edgecolor = 'black')
     plt.xlim(xx.min(), xx.max())
     plt.ylim(yy.min(), yy.max())
     patch0 = mpatches.Patch(color='#FF0000', label='apple')
     patch1 = mpatches.Patch(color='#00FF00', label='mandarin')
     patch2 = mpatches.Patch(color='#0000FF', label='orange')
     patch3 = mpatches.Patch(color='#AFAFAF', label='lemon')
     plt.legend(handles=[patch0, patch1, patch2, patch3])
     plt.xlabel('height (cm)')
     plt.ylabel('width (cm)')
     plt.title("4-Class classification (k = %i, weights = '%s')"
           % (n_neighbors, weights))    
     plt.show()
     
plot_fruit_knn(X_train, y_train, 5, 'uniform')




































