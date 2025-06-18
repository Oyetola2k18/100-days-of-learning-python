#learning about how to make your function to allow unlimited number of arguements


#lets see : def name(*args) args is just a naming convention programmers use, it can be any name
#it store the number of inputs you use and the data can be gotten same way we get data from tupples with loops

#the astericks * plays a huge role in allowing us to pull this off
def add(*numbers):
    sum = 0
    for num in numbers:
        sum+=num
     
    print(sum)

add(1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)

#the astericks packs all your input into a tuple and the name you specified ,in this case(numbers), 
# basically numbers = (your arguements)
#if it is *args
#args = (your arguements)
#this stuff is also called """UNlimited positional arguements"""


