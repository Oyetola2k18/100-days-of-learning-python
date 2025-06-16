# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas

read_nato = pandas.read_csv("Day26/Project/nato_phonetic_alphabet.csv")

nato_frame = pandas.DataFrame(read_nato)

word_list = {row.letter:row.code for (index, row) in nato_frame.iterrows()}

user_input = input("ENter a word: ").upper()

user_input_nato = [word_list[word] for word in user_input]

print(user_input_nato)