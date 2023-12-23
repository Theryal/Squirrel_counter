import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = []
cinnamon_squirrels = []
black_squirrels = []
black_number = 0
gray_number = 0
cinnamon_number = 0

list_of_furs = data["Primary Fur Color"].to_list()

for fur in list_of_furs:
    if fur == "Gray":
        gray_squirrels.append(fur)
        gray_number += 1
    elif fur == "Cinnamon":
        cinnamon_squirrels.append(fur)
        cinnamon_number += 1
    elif fur == "Black":
        black_squirrels.append(fur)
        black_number += 1
print(gray_squirrels)
print(gray_number)

# Create new csv containing color and total amount of the squirrels in that color
new_dict = {
    "fur_color": ["gray", "cinnamon", "black"],
    "squirrel_number": [gray_number, cinnamon_number, black_number],
}
nice_data = pandas.DataFrame(new_dict)
nice_data.to_csv("new_data.csv")

