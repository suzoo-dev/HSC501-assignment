from statsbombpy import sb
import pandas as pd
import json

'''
Search the GitHub for the England games and then download the files locally to help running the program in the future.
'''

# print(sb.competitions()) # Look through competitions and get the IDs for Euro 2024

# print(sb.matches(competition_id=55, season_id=282)) # Get the match ID for the final of the Euro 2024 competition

events = sb.events(match_id=3943043) # Get the Events of the final of Euro 2024
# events.to_csv("./data/england_events/3943043.csv") # Store the events in a csv file

# events = sb.events(match_id=3930163) # Serbia
# events.to_csv("./data/england_events/3930163.csv") 

# events = sb.events(match_id=3930171) # Denmark
# events.to_csv("./data/england_events/3930171.csv") 

# events = sb.events(match_id=3930181) # Slovenia
# events.to_csv("./data/england_events/3930181.csv") 

# events = sb.events(match_id=3941017) # Slovakia
# events.to_csv("./data/england_events/3941017.csv") 

# events = sb.events(match_id=3942227) # Switzerland
# events.to_csv("./data/england_events/3942227.csv") 

# events = sb.events(match_id=3942819) # Netherlands
# events.to_csv("./data/england_events/3942819.csv") 

# events = pd.read_csv("./data/england_events/3943043.csv")


match_id=3942819

# Load the 360 JSON file into a dataframe
json_data = json.load(open(f'./data/england_360/{match_id}.json'))
location_data = pd.json_normalize(data=json_data)

# Merge the event data to location data based on the event id
eventCols = ['id','player','location','timestamp', 'minute', 'type', 'possession_team']
merged = location_data.merge(events[eventCols], left_on='event_uuid', right_on='id', suffixes=('_360', '_events')).drop(columns=['id','visible_area'])

# Filter the data to only include Harry Kane events
harry_kane_events = merged[merged['player'] == 'Harry Kane']

# Function to find the deepest non teammate and non keeper location, then add to new list
def find_deepest(x):
  deepest = x['freeze_frame'][0]
  for y in x['freeze_frame']:
    if y['teammate'] == False and y['actor'] == False and y['keeper'] == False:
      if y['location'][0] > deepest['location'][0]:
        deepest = y
  return [x['event_uuid'], x['location'][0], format(deepest['location'][0], '.2f')]

# Initialise the result list
result = []

# Iterrate through the Harry Kane events and run find_deepest, appending the return to the result list
for index, x in harry_kane_events.iterrows():
  result.append(find_deepest(x))

# Convert the result list to a dataframe, name the columns and output to a csv file
pd.DataFrame(result, columns=['event_uuid', 'harry_kane_x_location', 'defender_x_location']).merge(merged, on='event_uuid').drop(columns=['freeze_frame','location']).to_csv(f'./data/results_{match_id}.csv', mode='w')

