"""Create a classic Rock, Paper, Scissors game in Python where the user can play against the computer.
Rules: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock"""
import random

def game(user, comp, check):  #Compare the user input and program Choice to determine the outcome
    if(check):
        print(f"{user} vs {comp}") # print the user and program Choice
        if(comp == user): 
            return 0
        # elif(comp == "R" and user == "S" or comp == "S" and user == "P" or comp == "P" and user == "R" ):
        #     return -1                  # U can use this instead of using below 3 elif block.
        elif(comp == "R" and user == "S"):
            return -1
        elif(comp == "S" and user == "P"):
            return -1
        elif(comp == "P" and user == "R"):
            return -1
        else:
            return 1
    else:
        return ValueError
  
def compare(x):      #Used to print the output 
    if(x == 1):
        print("You win")
    elif(x == -1):
        print("You loose")
    elif(x == ValueError):
        print("Please enter R or P or S")
    else:
        print("Its a draw")

def main():
    mylist = ["R", "P", "S"]
    Display_list = ["R for Rock", "P for Paper", "S for Scissors"]

    while True:                       #Game loop start 
        comp = random.choice(mylist)  #program Choice for the game
        for i in Display_list:        # print the game
            print(i)
        user = input(f"Enter your option:\n") #take the user input
        user = user.upper()
        check = user in mylist   # check if the user input is present in mylist or not.
        compare(game(user, comp,check))

        Play_More = input("Enter Y to play again. [OR] Enter any key to exit:\n")
        Play_More = Play_More.upper()

        check_condition = lambda x: True if x == "Y" else False  # Check if they want to play again
        if not check_condition(Play_More):
            print("Exiting.....")
            break

if __name__ == "__main__":
    main()
