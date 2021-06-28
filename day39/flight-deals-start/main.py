# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_mgr = DataManager()
fly_search = FlightSearch()

# Get all rows from spreadsheet
sheety_data = data_mgr.get_data()

# Iterate through rows and update iataCode
for row in sheety_data:
    row['iataCode'] = fly_search.get_iata_code(row['city'])

# Set data_mgr.data to updated data set
data_mgr.data = sheety_data

# Update the spreadsheet with new data
data_mgr.update_row()



