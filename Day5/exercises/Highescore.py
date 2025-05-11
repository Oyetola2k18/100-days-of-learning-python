#code to print ou the highest score from a list 
student_scores = input("Input a list of student scores\n").split()

#max() function prints out the highest value in a list 
#min() function prints out the lowest value in a list 
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_value = 0

for score in student_scores:
    #okay i made a mistake here or maybe i didnt ( i just didnt know the approach to take)
    if score > highest_value:
        highest_value = score

print(f"The Higest score is {highest_value}")