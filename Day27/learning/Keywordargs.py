#learning about kwargs , keyward arguements, here we make use of the double asteriicks **Kwargs

# def calculate(**kwargs):
#     print(kwargs)
#     # for key in kwargs:
#     #     print(f"{key} => {kwargs[key]}")

#     #or
#     for key,value in kwargs.items():
#         print(key,value)

# #so when i run this the **kwargs is like a dictionary that stored the keyword as key, and the value as the value in the dictionary

# calculate(add=3,multiply=5)
# #result
# #{'add': 3, 'multiply': 5}

# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n*=kwargs["multiply"]

#     print (n)
#     #2 + 3 = 5 *5 = 25


# calculate(2, add =3, multiply = 5)

class Car:
    def __init__(self,**kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        #in dictionaries we can get values by doing name.get(key)
        #it will return the value same as " self.model = kw["model"]"
        self.make = kw.get("make")
        self.model = kw.get("model")

        #the good thing about the get method is that if it searches for a key in a dictionary and 
        # doesnt find it, it just returns none and not an error unlike the traditional way of getting values 
        # from the dictionary
        self.color = kw.get("color")
        self.seats = kw.get("seats")

car = Car(make="nissan")

print(car.seats)
#this will return none now since we did not assign a value to our model attribute
