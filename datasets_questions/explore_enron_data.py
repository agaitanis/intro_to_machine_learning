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

number_of_people = len(enron_data)
number_of_features = len(enron_data.itervalues().next())
print 'Number of people =', number_of_people
print 'Number of features =', number_of_features

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

quantified_salary = 0
known_email_address = 0
unknown_total_payments = 0
poi_unknown_total_payments = 0
for name, data in enron_data.iteritems():
    if data['salary'] != 'NaN':
        quantified_salary += 1
    if data['email_address'] != 'NaN':
        known_email_address += 1
    if data['total_payments'] == 'NaN':
        unknown_total_payments += 1
        if data['poi'] == 1:
            poi_unknown_total_payments += 1

print 'Number of people with quantified salary', quantified_salary
print 'Number of people with known email address', known_email_address
print 'Number of people with unknown total payments', unknown_total_payments
print 'Ratio of people with unknown total payments', float(unknown_total_payments)/number_of_people
print 'Number of POIs with unknown total payments', poi_unknown_total_payments







