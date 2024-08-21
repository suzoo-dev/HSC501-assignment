'''
Program: Graded Programming Assignment
Author: Graham Fletcher
Loads in a data file containing data on Harry Kane's position and the deepest defender in the Euro 2024 final against Spain.
Calculates the median distance between Harry Kane and the defender.
'''
from load_data import getMatchId, loadFile
from analysis import getDistances, calculateMedian, verifyResult, calculateUpperLowerQuartiles

# Define the main function
def main():
    
    # Allow the user to select the match_id and load the match file
    match_id = getMatchId()
    f = loadFile(match_id)

    # Calculate the required distances to analyse and store these for later use
    distances = getDistances(f)

    # Analyse the data and print the results to the user
    median = calculateMedian(distances=distances)
    print(f'The median distance between Harry Kane and the defender is %0.2f metres.' % median)

    verifyResult(distances=distances, median=median)

    lower, upper = calculateUpperLowerQuartiles(distances=distances)
    print(f'The lower quartile was %0.2f and the upper quartile was %0.2f.' % (lower, upper))

    # Get user input to analyse another game or close the file
    again = input('Would you like to analyse another game? [y/n]: ')
    if again.lower() == 'y':
        main()
    else:
        f.close()

# Call the main function
main()