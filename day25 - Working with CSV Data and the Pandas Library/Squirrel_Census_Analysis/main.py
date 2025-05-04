# Goal is to count numbers of squirrels in each colors types and make a CSV with 2 columns : Colour and Number

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250427.csv")

c_cnt = 0
g_cnt = 0
b_cnt = 0
for color in data["Primary Fur Color"]:
    if color == "Cinnamon":
        c_cnt += 1
    elif color == "Gray":
        g_cnt += 1
    if color == "Black":
        b_cnt += 1

squirrels_colors_dict = {
    "Color": ["Cinnamon", "Gray", "Black"],
    "Number": [c_cnt,g_cnt,b_cnt]
}

results = pandas.DataFrame(squirrels_colors_dict)
results.to_csv("squirrels_colors_nb.csv")