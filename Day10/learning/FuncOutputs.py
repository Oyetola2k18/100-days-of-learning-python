#learning about functions with outputs , kinda like functions with return types


#functions with output

def format_name(f_name,l_name):
    first=f_name.title()
    last = l_name.title()
    return f"{first} {last}"

print(format_name("ZEPH","PackAge"))