#how gloabal keyword is useful with constants
#the naming convention in python for variables that you dont plant to modify (constants)
#it is to Write the name of the variable in ALL CAPS

def pi():
    return round(22/7,4)

PI_VALUE = pi()#constant 
URl= "https://www.GOOGLE.COM"
TWITTER_HANDLE = "@mo_ses.com"

def calc():
    global URl
    return URl

print(calc())