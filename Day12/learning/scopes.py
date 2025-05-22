#here we are learning about the concepts of scope(local and global scopes)
#name space: basically about that anything you name has a scope  for use (if that makes sense)
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope are scopes that are within functions

# def drink_potion():
#     potion_strength=2#local variable: can only be used within this function
#     print(potion_strength)

# drink_potion()
# print(potion_strength)#this would not run cuz we are trying to call a variable that is defined inside a another function

#global scope

player_health = 10#has a global scope and can be accessed anywhere within the file

def game():
    def drink_potion():#now a local function to game()
        potion_strength=2

        print(player_health)
    drink_potion()
