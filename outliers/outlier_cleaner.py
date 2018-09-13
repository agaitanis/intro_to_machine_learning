#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    
    for i in range(len(ages)):
        cleaned_data.append((ages[i][0], net_worths[i][0],
                             abs(predictions[i][0] - net_worths[i][0])))
    cleaned_data.sort(key=lambda x: x[2])
    cleaned_data = cleaned_data[:int(0.9*len(cleaned_data))]

    return cleaned_data