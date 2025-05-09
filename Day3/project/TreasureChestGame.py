#Final project for day3
#FInd the Bat signal

print('''
                                     ,.ood888888888888boo.,
                               .od888P^""            ""^Y888bo.
                           .od8P''   ..oood88888888booo.    ``Y8bo.
                        .odP'"  .ood8888888888888888888888boo.  "`Ybo.
                      .d8'   od8'd888888888f`8888't888888888b`8bo   `Yb.
                     d8'  od8^   8888888888[  `'  ]8888888888   ^8bo  `8b
                   .8P  d88'     8888888888P      Y8888888888     `88b  Y8.
                  d8' .d8'       `Y88888888'      `88888888P'       `8b. `8b
                 .8P .88P            """"            """"            Y88. Y8.
                 88  888                                              888  88
                 88  888                                              888  88
                 88  888.        ..                        ..        .888  88
                 `8b `88b,     d8888b.od8bo.      .od8bo.d8888b     ,d88' d8'
                  Y8. `Y88.    8888888888888b    d8888888888888    .88P' .8P
                   `8b  Y88b.  `88888888888888  88888888888888'  .d88P  d8'
                     Y8.  ^Y88bod8888888888888..8888888888888bod88P^  .8P
                      `Y8.   ^Y888888888888888LS888888888888888P^   .8P'
                        `^Yb.,  `^^Y8888888888888888888888P^^'  ,.dP^'
                           `^Y8b..   ``^^^Y88888888P^^^'    ..d8P^'
                               `^Y888bo.,            ,.od888P^'
                                    "`^^Y888888888888P^^'"         
      ''')
print("Welcome to archam city, Your mission is to find the source of the bat signal\n")

choice1 = input("You spawn at the center of a road, Go left or Right to find the Signal\n")
choice1_to_lowercase= choice1.lower()
if choice1_to_lowercase == "left":
    choice2 = input("okay dead end, Climb or Blast the wall(Climp or Blast)\n")
    choice2_to_lowercase = choice2.lower()
    if choice2_to_lowercase == "climb":
        choice3= int(input("After walking for sometime , you entered a building and you see 3 doors, only one lead to the roof of the building choose 1,2,3\n"))
        if  choice3 == 1:
            print("Good job , you've opened the door to where Batman's signal source is shinning from")
            print("End of Game (you got 1000 XP)")
        elif choice3 == 2:
            print("Game Over, Wrong door")
        elif choice3 == 3:
            print("Game Over, Wrong door")
        else:
            print("Invalid input")
    elif choice2_to_lowercase == "blast":
        print("you dont Have explosives dumbbo, Game Over")
    else:
        print("Invalid input")

elif choice1_to_lowercase =="right":
    print("Game Over, you chose the wrong route")
else:
    print("invalid input")