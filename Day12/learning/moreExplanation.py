#there a no block scopes

#this means that variables defined in if, for ,while and other blocks of code  are not affected by the namescope error

game_level = 3
def enemy():
    enemies = ["Skeleton","Zombies", "alien"]

    if game_level < 5:
        new_enemy = enemies[0]
    
    print(new_enemy)#this is a valid code as we can refer to a varibale defined in that if block

# print(new_enemy)#now  we cant refer to it , since its in a functioon and the "new_enemy" variable is local to the enemy  function
