'''
Module: load_data
Functions responsible for getting the users input for which file to load and then loading that file.
'''

import os

def loadFile(match_id):
    '''
    Input: filePath
    Output: file object
    Loads the data file and confirms with the user if the file was loaded correctly based on the row count and column names.
    '''

    # Get the current working directory and create data file path
    cwd = os.getcwd()
    dataFile = cwd + os.sep + 'data' + os.sep +  'results_' + str(match_id) + '.csv'

    # Check if the file exists and is a file
    if os.path.exists(dataFile) == False or os.path.isfile(dataFile) == False:
        print('Error loading file, either doesn\'t exist or is not a file.')
        exit()

    # Load in the data file
    f = open(dataFile, "r")
    
    # Initialise the line counter at -1 to account for the header
    lineCount = -1

    # Loop through the lines in the file and count the number of lines
    for line in f:
        lineCount += 1
    
    
    # Move to the start of the file and read the header
    f.seek(0)
    f.readline()

    # Show the file details to the user and confirm if the file is correct
    print(f'The file contains {lineCount} rows.')
    correct = input('Continue to analysis? [y/n]: ')

    # If the file is correct, return the file object
    if correct.lower() == 'y':
        return f 
    # If the file is not correct, print an error message and exit the program
    else:
        print('Please check the file and try again.')
        exit()

def getMatchId():
    '''
    Input: None
    Output: ID for the chosen match
    Uses a dictionary to store information about the available matches and allows the user to select the match to load.
    '''

    match_dict = {
        1 : ["1. Serbia (Group Stage)" , "3930163"],
        2 : ["2. Denmark (Group Stage)" , "3930171"],
        3 : ["3. Slovenia (Group Stage)" , "3930181"],
        4 : ["4. Slovakia (Round of 16)" , "3941017"],
        5 : ["5. Switzerland (Quarter-final)" , "3942227"],
        6 : ["6. Netherlands (Semi-final)" , "3942819"],
        7 : ["7. Spain (Final)" , "3943043"]
    }

    # Show the file details to the user and confirm if the file is correct
    print(f'England Euro 2024 Games:')
    for game, _ in match_dict.values():
        print(" " * 2 + game)
    game_num = int(input('Choose the game you want to view by entering the corresponding number: '))

    # Check user has entered a number between 1 and 7
    if game_num >= 1 and game_num <= 7:
        # Get the match_id from the chosen game number
        game, match_id = match_dict[game_num]

        return match_id
    else:
        print(f'Invalid entry of {game_num}, please try again.')
        getMatchId()