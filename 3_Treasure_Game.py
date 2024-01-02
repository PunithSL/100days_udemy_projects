
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
# input the direction from user
direction=input('''You're at a cross road. Where do you want to go? Type "left" or "right"\n''')
# converting uppercase letters to lowercase letter
direction=direction.lower()
# check the condition of direction
if direction=="left":
    island_wait=input('''You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n''')
    #input decision from user to choose swim or wait
    island_wait=island_wait.lower()
    if island_wait=="wait":
        door=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.\n Which colour do you choose?\n")
        #input decision from user to choose door
        door=door.lower()
        if door=="yellow":
            print("You found the Treasure! You Win!")
        else:
            print("You fell into a hole. Game Over.")
    else:
        print("You fell into a hole. Game Over.")
else:
    print("You fell into a hole. Game Over.")

