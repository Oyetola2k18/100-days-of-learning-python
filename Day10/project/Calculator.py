#code to create a calculator 

#functions the calculator performs
#add
from art import logo
def add(n1,n2):
    return n1 + n2

#subtract
def subtract(n1,n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1*n2

#divide

def divide(n1,n2):
    return n1/n2


operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

# answer = operations[operation_symbol](num1,num2)
# or 
# operation_function = operations[operation_symbol]
# then we can use the operation function as a function
# operation_function(num1,num2)
# print(f"{num1} {operation_symbol} {num2} = {answer}")

# operation_symbol = input("Pick an operation from the line above: ")
# operation_function2 =operations[operation_symbol]

# num3 = int(input("input the new number"))
# answer2 = operation_function2(answer,num3)

# print(f"{answer} {operation_symbol} {num3} = {answer2}")

#making use of recursion, this is when a function calls itself in itself lollll
def calculator():
    print(logo)
    end_calc = False
    num1=float(input("Input the first number:"))

    while end_calc==False:
        for opp in operations:
            print(opp)
        operation_symbol=input("Pick an operation from the line above: ")
        num2=float(input("Input the next number:"))

        operation_function = operations[operation_symbol]
        answer = operation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice =input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start the calculator again:")
        if choice == 'n':
            end_calc = True
            calculator()#if user says no, it exits the while loop and starts the function again
        if choice == 'y':
            num1 = answer
#where the program actually starts from
calculator()