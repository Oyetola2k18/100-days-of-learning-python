
# with open("Day25/weather_data.csv", mode="r") as file:
#     data = []
#     for each_row in file.readlines():
#         stripped_row=each_row.strip()

#         data.append(stripped_row)


#the csv library helps us in manipulating and cleaning csv files properly
# import csv

# with open("Day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

    # for row in data:
    #     the_tuple = tuple(row)
    #     if the_tuple[1] == "temp":
    #         pass
    #     else:
    #         temperatures.append(int(the_tuple[1]))
    
    # for row in data:
    #     if row[1] == "temp":
    #         pass
    #     else:
    #         temperatures.append(int(row[1]))
    
    # print(temperatures)

#the reason we will be using pandas instead of using the csv module, its cuz
# if we start working with files that are larger it can become stressful and painful

#the pandas library make it less stressful cuz it has inbuilt functions that does everything we 
# had to do manually when using the csv module

import pandas

data = pandas.read_csv("Day25/weather_data.csv")

#to get all the data om the temp row
# print(data["temp"])
# print(type(data))


#pandas has 2 primary data structures , (series and data frame)
#the data frame is like the normal excel sheet with rows and columns (its in 2 dimensions)
#the other one which is series , is just a single column in your table (in 1 dimension)

# data_dict = data.to_dict()
# print(data_dict)

#we can call just a column from the dataframe list and that how series

# temp_list = data["temp"].to_list()
#calculate average

# sum = 0
# for deg in temp_list:
#     sum+=deg

# average = sum/len(temp_list)
# print(round(average,2))

#the series.mean() function returns the average of a list 
# print(data["temp"].max())

# #getting data in a column
# # we can
# print(data["condition"])
# #or
# print(data.condition)
#pandas adds those column headers as attributes and also it is case sensitive


#getting a row 

# highest_temp = data["temp"].max()
# print(data[data.temp == highest_temp])
#basically i am saying, check my dataframe where the day is monday and print only that row

#to take it another step further
#lets say we want just one cell , (cell is an intersection of row and column)
#so lets say i want under monday, i want the condition

monday = data[data.day == "Monday"]

monday_temp = monday.temp

monday_temp_to_farenheit = (int(monday_temp)* (9/5)) + 32
print(monday_temp_to_farenheit)