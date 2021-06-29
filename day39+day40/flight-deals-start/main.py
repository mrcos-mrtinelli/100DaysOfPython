# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from datetime import datetime
from flight_search import FlightSearch
from flight_data import FlightData


HOME_AIRPORT = "LON"

data_mgr = DataManager()
flight_mgr = FlightSearch()


# Get all rows from spreadsheet
print("Getting destinations from spreadsheet.")
sheety_data = data_mgr.get_data()

print("Checking all destinations have IATA codes")
if data_mgr.needs_update():
    print("Loading missing IATA codes")
    row_ids = []
    for row in sheety_data:
        if row['iataCode'] == "":
            row['iataCode'] = flight_mgr.get_iata_code(row['city'])
            row_ids.append(row['id'])

    data_mgr.data = sheety_data
    data_mgr.update_rows(row_ids)
else:
    print("All Cities have IATA codes\n")

print("SEARCHING FOR FLIGHTS...\n")
for row in sheety_data:
    flight_query = FlightData(
        fly_from_code=HOME_AIRPORT,
        fly_to_code=row['iataCode'],
        date_from="29/06/2021",
        date_to="29/12/2021",
        price_to=row['lowestPrice']
    )
    flight_mgr.flight_query = flight_query.get_params()
    res = flight_mgr.get_flights()
    if res is not None:
        print(f"{res['cityTo']}: {res['price']}")

print("\nSearch Complete!")

