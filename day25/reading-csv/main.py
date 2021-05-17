import pandas

WEATHER_CSV = "weather_data.csv"

data = pandas.read_csv(WEATHER_CSV)

print((data[data.day == "Monday"].temp * 9/5) + 32)

# creating data frame with pandas

data_dict = {
    "students": ["Amy", "Brittany", "Cameron"],
    "grades": [99, 100, 69]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("data_frame.csv")
print(f"Data Frame:\n {data_frame}")