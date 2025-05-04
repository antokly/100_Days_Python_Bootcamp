import pandas

data = pandas.read_csv("weather_data.csv")

### Use Pandas basics Functions

print(type(data)) # DataFrame
print(type(data["temp"])) # Series

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list() # with a data serie entry
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)

# # OR
print(data["temp"].mean()) # median, mode, Max*

### Get data in Columns

print(data["condition"]) # Warning the key have to be exactly the same as the Raw Data
# # OR
# print(data.condition) # Here also

### Get Data in Row

print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

### Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
