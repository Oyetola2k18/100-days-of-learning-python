#learning how to loop through python data frame

student_dict = {
    "Students" :["Angela", "James", "Lily"],
    "score" : [56,76,98],
}

#looping through dictionary
# for (key,value) in student_dict.items():
#     print(key)

import pandas as pd

student_dataframe = pd.DataFrame(student_dict)

# print(student_dataframe)

#looping through a dataframe
# for (key, value) in student_dataframe.items():
#     print(value)

#pandas has its own inbuilt looping system to help with this 
#which is 


#loop throught rows of a data frame

#we use the itterrows() function to achieve this
for (index,row) in student_dataframe.iterrows():
    if row.Students == 'James':
        print(row.score)