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
from sklearn import svm

features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 
### These lines effectively slice the training dataset down to 1 percent of its original size, tossing out 99 percent of the training data. 
### You can leave all other code unchanged. What is the accuracy now?


clf = svm.SVC(kernel='linear')
acc = clf.fit(features_train, labels_train).score(features_test, labels_test)
print "accuracy:", acc


#########################################################


