# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

data_mgr = DataManager()
flight_mgr = FlightSearch()


# Get all rows from spreadsheet
sheety_data = data_mgr.get_data()

if data_mgr.needs_update():
    row_ids = []
    for row in sheety_data:
        if row['iataCode'] == "":
            row['iataCode'] = flight_mgr.get_iata_code(row['city'])
            row_ids.append(row['id'])
            print(f"updated: {row}")
    # data_mgr.data = sheety_data
    # data_mgr.update_rows(row_ids)
else:
    print("no updates needed!")


# for row in sheety_data:
#     flight_data_mgr = FlightData(
#         fly_from_code="LON",
#         fly_to_code=row['iataCode'],
#         date_from="29/06/2021",
#         date_to="29/12/2021",
#         price_to=row['lowestPrice']
#     )
#     flight_mgr.flight_query = flight_data_mgr.get_params()
#     response = flight_mgr.get_flight()
#     print(response)
