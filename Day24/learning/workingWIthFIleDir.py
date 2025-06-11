#Here i will be learning how to read and write to files or from files


# file = open("Day24/learning/my_file.txt")
# contents = file.read()

# print(contents)

# file.close()

#instead of doing it that way , we can use the with key word

# with open("Day24/learning/my_file.txt") as file:
#     #we can use any name infrom of that "as" keyword
#     content = file.read()

#     print(content)
    #here we dont need to write the file.close() line
    #after the end of this block, it automatically closes it 

#to write to our file 

# with open("Day24/learning/neweeer.txt", mode="a") as file:
#     pass
    #but make sure your file is writable first
    #to do that we set the mode in the open function to writable too

with open("../../Desktop/my_file.txt",mode="r") as file:
    content = file.read()
    print(content)

#learnt about the difference between Relative and absolute file paths 
#absolute file path starts from the c drive and navigates to the file you want to use or modify
#the relative file path starts from your working directory to where the file you want to modify is located
