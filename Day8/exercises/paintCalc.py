#calculate the amount of paint used to cover an area of a wall

#function that performs the calculation
import math
def paint_calc(height,width,cover):
    num_of_cans = (height * width) / cover
    print(f"YOU Will need {math.ceil(num_of_cans)} cans of paint")

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
paint_calc(height=test_h, width= test_w, cover= coverage)