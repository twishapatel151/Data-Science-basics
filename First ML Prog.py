# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 11:33:36 2018

@author: trupti.patel01
"""
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import  accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#Specify URL of data set 
#specify name of each columns while loading data
names=['sepal-length','sepal-width','petal-length','petal-width','class']
#load dataset 
dataset=pandas.read_csv("iris.csv",names=names)
#getting dimention of dataset
print(dataset.shape)
#for seeing first 20 rows of data
#print(dataset.head(20))
#get summary of data 
print(dataset.describe())
# number of instances (rows) that belong to each class
print(dataset.groupby('class').size())
# box and whisker plots 
dataset.plot(kind='box', subplots=True,layout=(2,2),sharex=False)
plt.show()
#create a histogram of each input variable to get an idea of the distribution
dataset.hist()
plt.show()
#can be helpful to spot structured relationships between input variables
scatter_matrix(dataset)
plt.show()
#We will split the loaded dataset into two, 80% of which we will use to train our models and 20% that we will hold back as a validation dataset.
array=dataset.values
X=array[:,0:4]
print(X.shape)

Y=array[:,4]
print(Y.shape)

# Test options and evaluation metric
validation_size=0.20
seed=7


X_train,X_test,Y_train,Y_test=model_selection.train_test_split(X,Y,test_size=validation_size,random_state=seed)
models=[]
models.append(('LR',LogisticRegression()))
models.append(('LDA',LinearDiscriminantAnalysis()))
models.append(('KNN',KNeighborsClassifier()))
models.append(('CART',DecisionTreeClassifier()))
models.append(('NB',GaussianNB()))
models.append(('SVM',SVC()))
# evaluate each model in turn
results=[]
names=[]
scoring = 'accuracy'
for name,model in models:
    kfold=model_selection.KFold(n_splits=10,random_state=seed)
    cv_results=model_selection.cross_val_score(model,X_train,Y_train,cv=kfold,scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg="%s: %f (%f)"%(name,cv_results.mean(),cv_results.std())
    print(msg)
# Compare Algorithms
fig=plt.figure()
fig.suptitle("Algorithm and comparision")
ax=fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)   
plt.show()

# Make predictions on validation dataset
knn=KNeighborsClassifier()
knn.fit(X_train,Y_train)
predictions=knn.predict(X_test)
print(accuracy_score(Y_test,predictions))
print(confusion_matrix(Y_test,predictions))
print(classification_report(Y_test,predictions))
