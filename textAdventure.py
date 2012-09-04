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


##################################################################################
# The main body of the program.  This part of the code will be what the 
# user interacts with.  This also includes all the main functions
# including those to check invintory, move the character and interact with
# the game.  
##################################################################################
class TextAdventure():

    # CHARACTERS
    # A collection of functions which allow the easy access of player stats 
    # including attack, defence and health.
    # TODO: determine the fighting mechanics
    # Main player (you)
    def player(att):
        a = 5
        d = 5
        hp = 7
        if att == 'a': return a
        elif att == 'd': return d
        elif att == 'hp': return hp

    # Main player's friend
    def fred(att):
        a = 9
        d = 4
        hp = 5
        if att == 'a': return a
        elif att == 'd': return d
        elif att == 'hp': return hp

    # Weak zombie
    def w_zombie(att):
        a = 2
        d = 2
        hp = 4
        if att == 'a': return a
        elif att == 'd': return d
        elif att == 'hp': return hp

    # Medium strength zombie
    def m_zombie(att):
        a = 4
        d = 3
        hp = 7
        if att == 'a': return a
        elif att == 'd': return d
        elif att == 'hp': return hp

    # Strong zombie
    def s_zombie(att):
        a = 8
        d = 6
        hp = 14
        if att == 'a': return a
        elif att == 'd': return d
        elif att == 'hp': return hp


    # MAIN FUNCTIONS
    # A function to check what the player has in it's invintory.
    # A loop compares the input (item) to each of the items in the list 
    # 'invintory.'
    def check_items(item):
        x = 0
        have = False
        for i in range(len(invintory)):
            x += 1
            if invintory[x-1] == item: 
                have = True
            else: 
                pass 
        return have
    
    # A function to check who is in the party. 
    # This works in the same way as the 'check_items' function.
    # TODO: make functions for each of the characters
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

    # A series of function for the movement of the player.  Each of the 
    # function returns the new respective position of the player.
    def move_left():
        pos_x += 1
        return pos_x
    def move_right():
        pos_x -= 1
        return pos_x
    def move_up():
        pos_y += 1
        return pos_y
    def move_down():
        pos_y -= 1
        return pos_y 
   
 
    # MAIN GAMEPLAY
    def main():
        print("*burp")
   
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
