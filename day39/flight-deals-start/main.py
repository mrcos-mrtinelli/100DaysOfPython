# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_mgr = DataManager()
fly_search = FlightSearch()

sheety_data = data_mgr.get_data()

data_with_iata = [fly_search.get_iata_code(city) for city in sheety_data]

data_mgr.data = data_with_iata
data_mgr.update_row()


