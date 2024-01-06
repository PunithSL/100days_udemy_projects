# import random module for computer chose
import random
# ASCII of Rock
Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
# ASCII of Paper
Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
# ASCII of Scissors
Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Run until user Enter N (No) 
while True :
    choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    # input choose from user
    game_option=[Rock,Paper,Scissors]
    print(game_option[choose])
    computer_choose=random.randint(0,2)
    # Random chose of Computer in range of 0 to 2
    print("Computer chose\n")
    print(game_option[computer_choose])
    # Condition for Game
    if choose==computer_choose:
        print("Tie ?")
    elif choose==0:
        if computer_choose==1:
            print("You lose")
        else:
            print("You Win!")
    elif choose==1:
        if computer_choose==2:
            print("You lose")
        else:
            print("You Win!")
    elif choose==2:
        if computer_choose==0:
            print("You lose")
        else:
            print("You Win!")
    # Play again or Not Condition
    try_agin=input("Try Again ? (Y/N):\n").lower()
    if try_agin=='n':
        break



