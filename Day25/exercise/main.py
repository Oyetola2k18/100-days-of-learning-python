#code to clean New york city central park data

import pandas

#furcolor(primary fur color)

squirel_data = pandas.read_csv("Day25/exercise/squirelData.csv")
fur_color = squirel_data["Primary Fur Color"]

fur_colors_list = fur_color.to_list()
# print(fur_colors_list)
num_of_gray = 0
num_of_red =0
num_of_black =0

for color in fur_colors_list:
    if color == "Gray":
        num_of_gray+=1
    elif color == "Cinnamon": #we are taking cinnamon as red
        num_of_red+=1
    elif color == "Black":
        num_of_black+=1
    else:
        pass

# print(f"number of black = {num_of_black}")
# print(f"number of red = {num_of_red}")
# print(f"number of grey = {num_of_gray}")

final_dict = {
    "Fur color": ["grey","black","red"],
    "COunt": [num_of_gray,num_of_black,num_of_red]
}

#converting final dictionary to csv file
final_dict_csv = pandas.DataFrame(final_dict)

final_dict_csv.to_csv("Day25/exercise/cleaned_squirrel_data.csv")