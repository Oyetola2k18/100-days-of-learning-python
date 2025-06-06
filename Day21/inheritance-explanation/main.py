#Today we are learning about another great concept under OOP which is inheritance

#syntax for inheritance
#if we have a class ANimal and another class fish wants to inherit properties from the animal class
#you do
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("INhale exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()


    def swim(self):
        print("MOVING IN WATER")
    
    def breathe(self):
        super().breathe()
        print("Under water")
    



nemo = Fish()

# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)
Fish.breathe(nemo)