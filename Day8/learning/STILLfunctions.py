#more explanation about functions
#learnt about positional arguments which is the default way of passing values to a function
#KEYWORD ARGUMENTS IS A WAY OF passing values to a function and also speciffying which parameter belongs to each value

def  greet_with(location,name):
    print(f"Hello {name}")
    print(f"How is it like in {location}")


greet_with(name="Moses",location="Lagos")