#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print "number of datapoints:", len(enron_data)
print "number of features:", len(enron_data["SKILLING JEFFREY K"])
poi = 0
for p in enron_data:
    poi += enron_data[p]['poi']
print "number of poi:", poi 
print "total stock value for James Prentice:", enron_data['PRENTICE JAMES']['total_stock_value']
print "total messages from Wesley Colwell to Pois:", enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print "total exercised stock options by Jeff Skilling:", enron_data['SKILLING JEFFREY K']['exercised_stock_options']
