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

#TODO: 
#       rules/about
#       walking around/story -> grid system

# IMPORT STATMENTS
import random
import readline
import pygame

# DECLARING VARIABLES    
# The items that the player starts the game with

invintory = ['ps3 controller', 'pliers', 'foam nunchuks', 'water']
money = 20
party = ['you']
pos_x = 0
pos_y = 1
pygame.init()

#MAPS
map_base = '''
                    ----------------
                    |              |__
                    | upstairs     |__  outside
                 == |              |
--------------- ==  ------|   |-----
|             |==         |   | 
|downstairs   |       ----     ----
|             |      | bedroom     |
--  -----------      --------------
  |  |
--|  |-------
| bathroom  |
-------------
'''


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

# A function to check the position of the player
def check_pos():
    global pos_x
    global pos_y
    if pos_x < 0:
        print("Hey, you steped out of line.  No worries, I put you back")
        pos_x = 0
    if pos_y < 0:
        print("Hey, you steped out of line.  No worries, I put you back")
        pos_y = 0


 
# A function that defines fighting
# For a description on how fighting works, read the README file.
def fight():
    # A collection of definitions for the players stats including attack (a),
    # defence (d) and health (hp).
    # Main player (you)
    you_a = 5.0   
    you_d = 7.0
    you_hp = 7.0
    # Main player's friend
    fred_a = 9.0
    fred_d = 5.0
    fred_hp = 10.0 
    # Zombie one
    zomb_a_one = 4.0
    zomb_d_one = 4.0 
    zomb_hp_one = 7.0
    # Zombie two
    # NOTE:  There is no need to define zomb_a_two or zomb_a_three 
    zomb_d_two = 4.0 
    zomb_hp_two = 7.0

    num_zomb = random.randint(1,2)	# Determines the number of zombies
    turn = 0		       	        # Initializes turns
    fight = True                        # Initializes loop
    print("watch out, there are " + str(num_zomb) + " zombies!")

    while fight == True:
        turn += 1        # Increases value of turn to create a psudo turntable 
        go = turn  % 2	 # Determines if it is player or zombie turn

        # If the number of zombies is less than three this will set the hp of the other zombies to zero
        if num_zomb == 1:	
            zomb_hp_two = 0
        else:
            pass

        # Whe you kill the zombie(s)
        if zomb_hp_one <= 0 and zomb_hp_two <= 0:	
            print("you defeted the brain sucker")
            break
        # When the zombie(s) kills you
        if you_hp <= 0:	 
            print("FAILed, no soup for you")
            break
 
        if go == 1:	 			# Players turn
           super_att = random.randint(1,5)	# Determines the strength of att
           if super_att == 1:
               you_a = 15.0
           elif super_att == 2:
               you_a = 10.0
           elif super_att == 3:
               you_a = 30.0
           elif super_att == 4:
               you_a = 1.0
           else: 
               you_a = 5.0
          
           # Recives input from the user regarding attack
           opt = input("do you wish to attack\n")
           if opt == 'yes':      
               # Recives input from the user regarding which zombie to attack
               dev = input("which zombie would you like to attack\n")
               if dev == "1":         
                   hit = you_a / zomb_d_one
                   zomb_hp_one -= hit
                   print("zombie 1 has " + str(int(zomb_hp_one)) + " hp left")
               elif dev == "2":         
                   hit = you_a / zomb_d_two
                   zomb_hp_two -= hit
                   print("zombie 2 has " + str(int(zomb_hp_two)) + " hp left")
               else: print("invalid input -> looks like you loose your turn")
           elif opt == 'no':
              print("you do not attack") 
           # If the user chooses to not fight
           elif opt == 'run':
              break
           else:
               print("Invalid input.  I'm just going to take that as a no.")
       
        elif go == 0:	 	 		# Computer turn
           att = random.randint(1,5)            # Determines if zombie attacks 
           super_att = random.randint(1,3)	# Determines the strength of att
           if super_att == 1:
               zomb_a_one = 14.0
           elif super_att == 2:
               zomb_a_one = 0.5 
           else: 
               zomb_a_one = 4.0

           # Zombie attacks
           if att == 1 or 2 or 3:
               hit = zomb_a_one/you_d 
               you_hp -= hit
               print("\nA zombie attacked and you have " + str(int(you_hp)) + " hp left")
           # Zombie does not attack
           else:
               print("\nThe zombie missed")

# MAIN GAMEPLAY
def main():

    global pos_x
    global pos_y

    print("\nYou are in a basement, a bit confued.  You have just been playing video games for 47.3 hours, only pausing to dail up the pizza delivery guy to get you another extra large pizza with only cheese.  *SHPAOOSH.\n") 
    input() 
    print("Dammit, there goes to super cool gaming system (play system 3.5.7).\n")
    input()
    print("*Turn on the news \n \"...and now we bring you breaking news:  zombies have taken over the local Walemart.  Now the only safe place to hide is the island...\" *RING.")
    input()
    print("You:\"Hello\"\n")
    input()
    print("Fred:\"Dude, there is a zombie outbreak\"\n")
    input()
    print("You: \"I know, what are we going to do\"\n")
    input()
    print("Fred: \"meet me at the park across the street\"\n")
    input()
    print("You: \"Alright\"\n")

    game = True		# Initializes the variable game to True
    while game == True:
        check_pos()
        dev = input("\nwhat are you going to do\n").lower()
        
        if dev == "quit":      	 # Quits the game
            game = False
        # For moving around
        elif dev == "left":
           pos_x -= 1
        elif dev == "right":
           pos_x += 1
        elif dev == "up":
           pos_y += 1
        elif dev == "down":
           pos_y -= 1
        # Prints a map base on position
        elif dev == "map":     
            if pos_x <= 2 and pos_y <= 2:
                print(map_base)
            else:
                print("no map")
        # Misc commands
        elif dev == "check items": # Displays items in invintory
            print(invintory)
        else: 
            print("what is this \"" + dev + "\" nonsense")
       
main()
# The introduction
#TODO: uncomment the introduction
#print("\n \n \n \nHello and welcome to the game.  It is about you!  Also about zombies.  If this is your first time playing you should type in 'how to play' so that you can learn to play the game.  If you played the game before, took a look at the code before playing or are exceptional at guessing, type in 'start' to begin.") 
#opt = input()
#if opt == 'start': 
#    main()
#elif opt == 'how to play':
#    print("HOW TO PLAY:  \nFIGHTING:  You can also fight zombies in this game.  At any one time you can fight one or two zombies but keep in mind, your friend in fat and lazy and does not help you while you fight.  First you will be told how many zombies you are fighting.  Then you can choose to fight by typeing in \"yes\" or you can choose to get away from the fight by typeing in \"run\" and \"no\" to do niether.  To choose which zombie you wish to attack, press \"1\" for zombie one, or \"2\" for zombie two.  That is it.  Also, sometimes you can kill a zombie into negative hp.  Don't worry about that, you are just that awesome.")
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
