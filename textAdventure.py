###########################################################################
##                                                                        #
##! /usr/bin/env python3                                                  #
##Prorgammed by: Sophia Castellarin                                       #
##Thursday, August 30, 2012                                               #
##Program Desciption: A text adventure game                               #
##                                                                        #
###########################################################################

#--------------------------------------------------------------------------------#
# STORY 
#    You play as a lowly nerd who must get out of the basement because you are 
# really hungry.  Little do you know that 3 months have past by while you were 
# playing Skyrim and surviving off old pizza and red bull.  In thoes three 
# months a lot has changed and in fact your dog is now a zombie, also, so is your 
# neigbour and most other people.  You must meeet a friend and together  
# escape to an anti-zombie base.
#--------------------------------------------------------------------------------#

# The items that you start the game with
invintory = ['ps3 controller', 'pliers', 'foam nunchuks', 'water']
money = 20

# A function to check what you have in your invintory
# A loop compares the input (item) to each of the items in the list 'invintory'
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

# runs the 'check_items' fuction and returns an output based on the invintory
have = check_items('pliers')
if have == True: print("you have that")
elif have == False: print("you do not have that")
else: print("something went horribly wrong")

