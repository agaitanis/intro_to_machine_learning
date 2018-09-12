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

print 'Number of people =', len(enron_data)
print 'Number of features =', len(enron_data.itervalues().next())

pois = 0
for name, data in enron_data.iteritems():
    pois += data['poi']
print 'Number of POIs =', pois

f = open('../final_project/poi_names.txt')
text = f.read()
print 'Total number of POIs =', text.count('(n)') + text.count('(y)')
f.close()

print 'Total stock value belonging to James Prentice =', enron_data['PRENTICE JAMES']['total_stock_value']

print 'Number of messages from Wesley Colwell =', enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print 'Value of stock options exercised by Jeffrey K Skilling =', enron_data['SKILLING JEFFREY K']['exercised_stock_options']

