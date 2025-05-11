#learning how to use for loops with the range operator
#syntax is range(a,b) from a to b but not the last digit whcih is b
#if we want to increment the strep by a larger number from 1 which is the default , we will need a 3rd argument
#range(1,10,2) so it prints in twos
# output will be 1, 3,5,7,9 (you know b will not be mentioned )


#this code will print out the sum of all numbers from 1 to 100 (i wrote 101 cuz i wanted it to stop at 100)doesn't really make sense 

sum = 0
for number in range(1,101):
    sum += number
print(sum)