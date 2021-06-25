#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

# data_mgr = DataManager()
# sheety_data = data_mgr.data['destinations']
sheety_data = [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
 {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
 {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
 {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
 {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
 {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
 {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
 {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 260},
 {'city': 'Cape Town', 'iataCode': '', 'id': 10, 'lowestPrice': 378}]
print(f"sheety_data: {len(sheety_data)}")
fly_search = FlightSearch()
new_sheety_data = [fly_search.get_iata_code(city) for city in sheety_data]
print(f"new_sheety_data: {len(new_sheety_data)}")
print(new_sheety_data)



