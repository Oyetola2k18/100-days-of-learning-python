#learning about modifying global scopes
enemies = 1

def increase_enemies():
    # global enemies
    # enemies = 2 #to actually modify the main "enemies" variable , you have to explicitly state it
    # print(f"enemies inside function: {enemies}")
    return enemies+1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")