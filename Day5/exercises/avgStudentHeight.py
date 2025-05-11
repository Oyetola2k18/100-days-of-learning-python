#code to calculate th eaverage height of students
#we can use the sum() function to get the addition of all the elements in a list(numbers)
student_height = input("Input a list of student heights\n").split()


for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

#to calculate the sum of each height inputed
sum = 0
num_of_students = 0
for height in student_height:
    sum = sum + height
    num_of_students += 1 #this acts as a counter for how many times the code runs
    #now to get the number of items in the list without using len

average_height = sum // num_of_students
print(f"The average for the height of the students is {average_height}")