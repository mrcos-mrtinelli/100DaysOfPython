import pandas

WEATHER_CSV = "weather_data.csv"

data = pandas.read_csv(WEATHER_CSV)

print((data[data.day == "Monday"].temp * 9/5) + 32)
