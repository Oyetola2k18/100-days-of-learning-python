with open("Day26/exercise/exercise3/file1.txt") as file1:
    data1 = file1.readlines()

with open("Day26/exercise/exercise3/file2.txt") as file2:
    data2 = file2.readlines()

d1 = [int(num) for num in data1]
d2 = [int(num) for num in data2]


result =[num for num in d1  if num in d2] 
print(result)