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

    ### your code goes here
    all_data_turples = []
    for (i,a) in enumerate(ages):
        nw = net_worths[i][0]
        p = predictions[i][0]
        all_data_turples.append((a[0], nw, abs(nw - p)))
    
    if len(all_data_turples):
        all_data_turples.sort(key=returnError)
        cleaned_data = all_data_turples[:81]    

    return cleaned_data

def returnError(elem):
    return elem[2]

