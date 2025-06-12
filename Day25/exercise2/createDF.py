#Creating our own data frame
 
import pandas

data_dict = {
    "students": ["Amy", "James","Angela"],
    "scores": [76,56,65]
}

#call the pandas module and initialize the DataFrame clase with your data dictionary

data = pandas.DataFrame(data_dict)
print(data)

#we can also create a csv file from that
data.to_csv("Day25/newpackage.csv")