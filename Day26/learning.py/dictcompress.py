#list comprehension but in dictionaries
#should we say dictionary comprehension lol
#syntax:new_value for item in list}
#or
# new_dict = {new_key
# new_dict = {new_key:new_value for (key,value) in dict.items()}
#to add conditions
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

#with dict comprehension
student_scores = {student:random.randint(1,100) for student in names}

#The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.


#without dict comprehension
# student_scores = {}
# for name in names:
#     student_scores[name] = random.randint(1,100)
#this dictionary is created by doing : for each students name in the name list, you assign a tandom value to the students name in the list
print(student_scores)

#okay lets use our new student scores dictionary to create another dictionary

passed_students = {name:score for (name,score) in student_scores.items() if score >= 60}
print(passed_students)