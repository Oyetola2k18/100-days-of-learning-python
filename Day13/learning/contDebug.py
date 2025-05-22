#continue debugging
# Play Computer
# year = int(input("What's your year of birth?"))
#the bug here is that the code is not including a case where the year is 1994
#if it is 1994/1980 , none of the if statements go through
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

#fix
# if year >= 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")


#fixed
# age = int(input("How old are you?"))#another errorr is the type error
# if age > 18:#the issue here was an indentation problem
#     print(f"You can drive at age {age}.")
#also didnt add formated strings

#Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# print(pages)
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])