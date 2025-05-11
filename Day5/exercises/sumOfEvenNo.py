#code to  calculate thee sum of even number from 1to 100

total_of_even = 0

# for n in range(0,101,2):
#     total_of_even += n
# print(total_of_even)

#or

for x in range(0,101):
    if x % 2 ==0 :
        total_of_even += x
print(total_of_even)