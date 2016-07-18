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
### Keep the training set size and rbf kernel from the last quiz, but try several values of C (say, 10.0, 100., 1000., and 10000.). 
### Which one gives the best accuracy?

from sklearn import svm

features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 

for C in [10, 100, 1000, 10000]:
    clf = svm.SVC(kernel='rbf', C=C)
    acc = clf.fit(features_train, labels_train).score(features_test, labels_test)
    print "C:", C, "accuracy:", acc


#########################################################


