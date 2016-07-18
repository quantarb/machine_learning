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
### Now that you have optimized C for the RBF kernel, go back to using the full training set. 
### In general, having a larger training set will improve the performance of your algorithm, so (by tuning C and training on a large dataset) we should get a fairly optimized result. 
### What is the accuracy of the optimized SVM?
from sklearn import svm

clf = svm.SVC(kernel='rbf', C=10000)
acc = clf.fit(features_train, labels_train).score(features_test, labels_test)
print "accuracy:", acc


#########################################################


