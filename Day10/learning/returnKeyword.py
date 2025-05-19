#the return keywork marks the end of a function
def format_name(f_name,l_name):
    if f_name == "" or l_name== "":
        return "Empty input"
    first=f_name.title()
    last = l_name.title()
    return f"{first} {last}"

print(format_name(input("What is your frst name?"),input("what is yout last name?")))