'''
Module: analysis
Functions to calculate the distance values, the median of those values and then verify the result with Numpy.
'''
import numpy as np

def getDistances(f):
    '''
    Input: file object
    Output: list of distances
    Gets the distances between Harry Kane and the defender.
    '''

    # Initialise the distance list
    distances = []
    
    # Loop through the lines in the file and get the distances
    for line in f:
        # Split the line into a list of values
        values = line.split(',')
        # Get the distance between Harry Kane and the defender
        distance = float(values[3]) - float(values[2])
        # Add the distance to the list converted to metres
        distances.append(distance / 0.875)

    return distances

def calculateMedian(distances):
    '''
    Input: list of distances
    Output: median distance
    Calculates the median distance between Harry Kane and the defender.
    '''
    
    # Sort the list of distances
    distances.sort()

    # Get the median distance
    middle = len(distances) // 2
    
    if len(distances) % 2 == 1:
        median = distances[middle]
    else:
        median = (distances[middle] + distances[middle - 1]) / 2

    return median

def verifyResult(distances, median):
    '''
    Input: list of distances, median distance
    Output: None
    Uses numpy to calculate the median distance and compare to the calculated median.
    Displays the result to the user.
    '''

    # Calculate the median distance using numpy
    distancesArray = np.array(distances)
    npMedian = np.median(distancesArray)
    
    print('Numpy calculated the median as %0.2f metres.' % npMedian)

    # Check if the calculated median is equal to the given median
    if npMedian == median:
        print(u'Analytic verification: \u2714 correct!')
    else:
        print(u'Analytic verification: \u2718 incorrect.')

def calculateUpperLowerQuartiles(distances):
    '''
    Input: list of distances
    Output: upper and lower quartiles ie 25th and 75th percentiles
    Uses numpy to calculate the upper and lower quartiles
    '''
    # print(distances)
    distancesArray = np.array(distances)
    return np.percentile(distancesArray, [25, 75])