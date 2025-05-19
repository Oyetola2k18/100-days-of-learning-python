#code to create a calculator 

#functions the calculator performs
#add
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

num1=int(input("Input the first number:"))
num2=int(input("Input the Second number:"))

for opp in operations:
    print(opp)
operation_symbol=input("Pick an operation from the line above: ")

answer = operations[operation_symbol](num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")