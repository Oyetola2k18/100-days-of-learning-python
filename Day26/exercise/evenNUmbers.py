#list comprehension exercise part 2
numbers = [1,1,2,3,5,8,13,21,34,55]

#print all even numbers from that list 

result = [num for num in numbers if num % 2 == 0]
print(result)