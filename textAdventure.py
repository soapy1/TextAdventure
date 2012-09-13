###########################################################################
##                                                                         #
##! /usr/bin/env python3                                                   #
## Prorgammed by: Sophia Castellarin                                       #
## Thursday, August 30, 2012                                               #
## Program Desciption: A text adventure game                               #
##                                                                         #
###########################################################################


##################################################################################
#--------------------------------------------------------------------------------#
# STORY 
#    You play as a lowly nerd who must get out of the basement because you are 
# really hungry.  Little do you know that 3 months have past by while you were 
# playing Skyrim and surviving off old pizza and red bull.  In thoes three 
# months a lot has changed and in fact your dog is now a zombie, also, so is your 
# neigbour and most other people.  You must meeet a friend and together  
# escape to an anti-zombie base.
#--------------------------------------------------------------------------------#
##################################################################################


# IMPORT STATMENTS
import random

# DECLARING GLOBAL VARIABLES    
# The items that the player starts the game with
invintory = ['ps3 controller', 'pliers', 'foam nunchuks', 'water']
money = 20
party = ['you']
# The position that the player starts the game in
pos_x = 0
pos_y = 0

# MAIN FUNCTIONS
# A function to check what the player has in it's invintory.
# A loop compares the input (item) to each of the items in the list 
# 'invintory.'
def check_items(item):
    x = 0			    # Initializes the value of x
    have = False	            # Initializes the value of have
    for i in range(len(invintory)): # A loop that lasts the length of the list
        x += 1
        if invintory[x-1] == item:  # Cycles through the items in the list
            have = True             # If a match is found have is set to true
        else: 
            pass 
    return have			    # Returns the value of have
  
# A function to check who is in the party. 
# This works in the same way as the 'check_items' function.
def check_party(name):
    x = 0
    have = False
    for i in range(len(party)):
        x += 1
        if party[x-1] == name: 
            have = True
        else: 
            pass 
    return have
 
# A function that defines fighting
def fight():
    # A collection of definitions for the players stats including attack (a),
    # defence (d) and health (hp).
    # Main player (you)
    you_a = 5   
    you_d = 7 
    you_hp = 7
    # Main player's friend
    fred_a = 9
    fred_d = 5
    fred_hp = 10 
    # Weak zombie
    weakZomb_a = 2
    weakZomb_d = 2
    weakZomb_hp = 4
    # Medium strength zombie
    medZomb_a = 2
    medZomb_d = 6
    medZomb_hp = 7
    # Strong zombie
    strZomb_a = 8
    strZomb_d = 4
    strZomb_hp = 9 

    turn = 0		 # Initializes turns
    fight = True         # Initializes loop
    while fight == True:
        turn += 1        # Increases value of turn to create a psudo turntable 
        go = turn  % 2	 # Determines if it is player or zombie turn
        if go == 1:	 # Players turn
           print("do you wish to attack")
           if input() == "yes":
               hit = you_a / weakZomb_d
               weakZomb_hp -= hit
               print("the zombie has " + str(weakZomb_hp) + " hp left") 
           elif input() == "no":
              print("you do not attack") 
           else:
               print("Invalid input.  I'm just going to take that as a no.")
           if weakZomb_hp == 0:
                print("you defeted that brain sucker")
                break
        elif go == 0:	 # Computer turn
            att = random.randint(1,3)
            if att == 1:
                hit = 1 
                you_hp -= hit
                print("\nThe zombie attacked and you have " + str(you_hp) + " hp left")
            elif att == 2 or 3:
                print("the zombie missed")
            if you_hp == 0:
                print("failed, no soup for you")
                break         
            #TODO:  finish writing the code 
# MAIN GAMEPLAY
def main():
    print("*burp")
       
fight() 

    # The introduction
    #TODO: uncomment the introduction
    #print("\n \n \n \nHello and welcome to the game.  It is about you!  Also about zombies.  If this is your first time playing you should type in 'how to play' so that you can learn to play the game.  If you played the game before, took a look at the code before playing or are exceptional at guessing, type in 'start' to begin.") 
    #opt = input()
    #if opt == 'start': 
    #    main()
    #elif opt == 'how to play':
    #    print("HOW TO PLAY:")
    #    if input() == 'start':
    #        main()
    #    elif input() == 'quit':
    #       exit 
    #else:
    #    print("Sorry, a zombie bit off the part of the code that was suppose to understand that.  HAAAA SHUTING DOWN.")
    
    # TESTING CODE
    # runs the 'check_items' fuction and returns an output based on the invintory 
    #have = check_items('pliers')
    #if have == True: print("you have that")
    #elif have == False: print("you do not have that")
    #else: print("something went horribly wrong")
##################################################################################
