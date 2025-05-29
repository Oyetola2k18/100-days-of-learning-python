#working on How to create classes

#we want to leave our class empty but python keeps throwing error because it expects an indentation
# we use the pass key in place of any code , it does nothing it just tells the compiler to go to the next line


#basic examples of cases : Pascal casing (MyNameIsMoses), camel casing(myNameIsMoses), and snake casing (my_name_is_moses)
class User:
    #self is the actuall object being created or being initialized
    #the name of the parameter can be different from the name of the attribute

    def __init__(self, user_id,username):
        self.id = user_id
        self.username = username
        self.follower = 0 #setting a default value for follower
        self.following = 0

    def follow(self, user):
        user.follower +=1
        self.following +=1
# user_1 =User()
# #adding attributes to our class
# user_1.id = "001"
# user_1.username = "JackBoeur"
# print(user_1.username)

# user1 = User(5,"Ogunyemi Oyetola")
# print(user1.id)#we call it here according to the attribute name , not the parameter's name 

# print(user1.username)
#in python we use the def ___init__(self): function as a construction
#when an object is created , it initialized them with attributeds

user1 = User("001","PackageBoy")
user2 =User("002","GehGeh")

print(user1.follower)
print(user1.following)

print(user2.follower)
print(user2.following)
user1.follow(user2)
print("\n")
print(user1.follower)
print(user1.following)

print(user2.follower)
print(user2.following)