import pandas

# WEATHER_CSV = "weather_data.csv"
#
# data = pandas.read_csv(WEATHER_CSV)
#
# print((data[data.day == "Monday"].temp * 9/5) + 32)

# creating data frame with pandas

# data_dict = {
#     "students": ["Amy", "Brittany", "Cameron"],
#     "grades": [99, 100, 69]
# }
#
# data_frame = pandas.DataFrame(data_dict)
# data_frame.to_csv("data_frame.csv")
# print(f"Data Frame:\n {data_frame}")


SQUIRREL_CENSUS_CSV = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"


# grouped_by_fur_color = data.groupby(by=["Primary Fur Color"], dropna=True).transform("count")
# data_dict[color] = data[data["Primary Fur Color"] == color].count()[0]
data = pandas.read_csv(SQUIRREL_CENSUS_CSV)
fur_colors = (data["Primary Fur Color"]).dropna().unique()
data_dict = {
    "Fur Color": [],
    "Count": []
}
for color in fur_colors:
    data_dict["Fur Color"].append(color)
    count = data[data["Primary Fur Color"] == color].count()[0]
    data_dict["Count"].append(count)

data_frame = pandas.DataFrame(data_dict)

data_frame.to_csv("squirrel_count.csv")