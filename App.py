import hulk #import hulk module to access its function
import ironman #import ironman module to access its function
import Game #import Game module to access its function



def main(): #main fuction
   
    player_name = str(input("What is your name? ")) #a variable to store username
    print ("Welcome to the dice game {}! Here you will battle it out to save the universe from Thanos.".format (player_name))
    print ("Let the war begin!! There are 3 challenges in this game. \n Round 1: Find Infinity stone grenade. \n Round 2: Locate Soul Planet where you can find Thanos. \n Round 3: Defeat Thanos to save the universe")
    role = str(input("Choose your character? \n Ironman or Hulk ")) #variable to store chossen character
    print("Nice one {}!!".format (player_name))
    print("You're playing this game as {} \n Your Powers:".format (role))
    if role.lower() == "ironman":
            print("  ",ironman.show()) #accessing show() function from ironman module
    if role.lower() == "hulk":
            print("  ",hulk.show())  #accessing show() function from hulk module
            
    Game.round_one() #method call from Game module

if __name__ == "__main__":
    main()