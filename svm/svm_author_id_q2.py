#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###



### Place timing code around the fit and predict functions, like you did in the Naive Bayes mini-project. 
### How do the training and prediction times compare to Naive Bayes?

from sklearn import svm
clf = svm.SVC()

print "SVC"
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"


t0 = time()
predictions = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"


print "accuracy:", clf.score(features_test, labels_test)




from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

print "GaussianNB"
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"


t0 = time()
predictions = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"


print "accuracy:", clf.score(features_test, labels_test)
#########################################################


