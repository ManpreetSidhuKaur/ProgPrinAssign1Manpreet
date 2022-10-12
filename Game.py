

import random   #random module : provides access to functions that support many operations

def round_one(): #round_one method 
    print("Welcome to challenge 1! In order to win Infinity granade you need to roll lower than a 3!")
    print("Are you ready? Y/N ")
    output = str(input("")) #user input
    if output.lower() == "y":
        dice = random.randint(1, 6) #returns random integer in range(1,6) including both numbers.
        if dice < 3:
            print(dice)
            print("Hurray!!! You got a hold of Infinity Granade!! You can proceed to next level where you need to find soul planet!!")
            round_two() #method call
        if dice > 3:
            print(dice)
            print("You lose!! better luck next time")
    if output.lower() == "n":
        print("Hope to see you again")

def round_two(): #round_2 method
    print("Welcome to challenge 2! To get through this round you need to roll higher than a 3!")
    print("Are you ready? Y/N ")
    output = str(input("")) #palyer's input
    if output.lower() == "y":
        dice = random.randint(1, 6) #returns random integer in range(1,6) including both numbers.
        if dice >= 3:
            print(dice)
            print("You have won this round!! Now you have to fight Thanos in order to save the Universe!!")
            round_three() #method call
        if dice < 3:
            print(dice)
            print("You lose!! better luck next time")
    if output.lower() == "n":
        print("Hope to see you again")

def round_three(): #round_three method
    print("Welcome to the final round! To get through this round you need to roll a 6!")
    print("Are you ready? Y/N ")
    output = str(input("")) #user input
    if output.lower() == "y":
        dice = random.randint(1, 6) #returns random integer in range(1,6) including both numbers.
        if dice == 6:
            print(dice)
            print("Congratulations!! You saved the whole universe!!!")
        if dice != 6:
            print(dice)
            print("You lose!! better luck next time")
    if output.lower() == "n":
        print("Hope to see you again")

