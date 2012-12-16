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
# rules/about

# IMPORT STATMENTS
import random
import readline

# DECLARING VARIABLES    
# The items that the player starts the game with
stuffs = ['ps3 controller', 'pliers', 'foam nunchuks', 'water', 'food']
party = ['you']		# People you are travelling with
pos_x = 0		# Your starting position in the x axis 
pos_y = 1		# Your starting position in the y axis
you_hp = 15.0		# Your health.  This is put here so that you can determine your health while playing the game and use powerups to increase your health.

#MAPS
map_base = '''
                    ----------------
                    |              |__
                    | upstairs     |__  outside
                 == |              |
--------------- ==  ------|   |-----
|             |==         |   | 
|downstairs   |       ----     ----
|             |------| bedroom     |
--  -----------       -------------
  |  |
--|  |-------
| bathroom  |
-------------
'''

map_outside = '''
              ----------
              | gram's |           
              | house  |           
              |__    __|          ________
/\/\/\/\/\/\/\/\/|  | /\/\//\/\/ /    /|\ \ 
---------------------------------      |   |
                                      /|\  |
---------------------------------  (park)  |   
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\___  ___/
                                     | |
            (misc houses)                        
'''         
# STORY DIALOG
# Introduction to the game
def d_intro():
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

# When you reach outside
def d_outside():
    print("\nThere is nobody outside... wait, there is someone at the park across the street... perhaps it is Fred")
    input()
    print("Dude across the street: \"Hey, come quickly, there are zombies and when they come I won't help you\"\n") 
    input()

# When you get to the park
def d_park():
    print("\nFred: \"Dude, where have you been.  I've been waiting for you...\"")
    input()
    print("\"...  lets go.  We need to get to the store house.  It is safe there.\"")
    print("END PART I")

# MAIN FUNCTIONS
# A function to check what the player has in it's invintory.
# A loop compares the input (item) to each of the items in the list 
# 'stuffs.'
def check_items(item):
    x = 0			    # Initializes the value of x
    have = False	            # Initializes the value of have
    for i in range(len(stuffs)):    # A loop that lasts the length of the list
        x += 1
        if stuffs[x-1] == item:     # Cycles through the items in the list
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
    if pos_x == 2:
        d_outside()
    if pos_x == 8:
        d_park()

# A function that allows the player to search the surroundings for stuff
def search():    
    # Determines if you have too much stuff
    num_items = len(stuffs)
    if num_items < 7:
        i = random.randint(0, 15)
        # Determines if you find stuff 
        if i == 0 or 3:			# Find water
            print("you found water... in a reusable bottle... so eco friendly")
            stuffs.append("water")
        elif i == 1 or 5:		# Find food
            print("you found food, TASTY!")
            stuffs.append('food')
        elif i == 2:			# Find a weapon
            w = random.randint(0,2)
            if w == 0:
                print("you found foam nunchuks")
                stuffs.append('foam nunchuks')
            elif w == 1:
                print("you found a stick")
                stuffs.append('stick')
            elif w == 2:
                print("you found a pillow")
                stuffs.append("pillow")  
        else:
            print("You found nothing")
    else:
        print("You can't carry anything else.  If you want to pick something up, you need to drop something.")

# A function that allows player to drop items
def drop():
    print(stuffs)
    drop_item = input("\nEnter the index of the item you want to drop (use number keys and the first item is index 0)")
    stuffs.pop(int(drop_item))


# A function that defines fighting
# For a description on how fighting works, read the README file.
def fight():

    global you_hp

    # A collection of definitions for the players stats including attack (a),
    # defence (d) and health (hp).
    # Main player (you)
    you_a = 5.0   
    you_d = 7.0
    # Main player's friend
    fred_a = 9.0
    fred_d = 5.0
    fred_hp = 10.0 
    # Zombie one
    zomb_a_one = 5.0
    zomb_d_one = 4.0 
    zomb_hp_one = 7.0
    # Zombie two
    # There is no need to define zomb_a_two or zomb_a_three 
    zomb_d_two = 6.0 
    zomb_hp_two = 7.0

    # Determines if there are any weapons/ powerups
    have = check_items('foam nunchuks')
    if have == True:
        you_a += 1.5
        you_d += 0.5
    have = check_items('stick')
    if have == True:
        you_a += 3.0
        you_d += 1.0
    have = check_items('pillow')
    if have == True:
        you_a += 0.5
        you_d += 2.0
    else:
        pass

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
            print("FAILed, no banana bread for you")
            quit()
 
        if go == 1:	 			# Players turn
           super_att = random.randint(1,7)	# Determines the strength of att
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
           # If the user chooses to not fight there is a on in five chance that they will be able to run away
           elif opt == 'run':
              r = random.randint(0,5)
              if r == 0:
                  print("you got away")
                  break
              else:
                  print("son of very poop face, the zombies caught up to you")
                  pass
           else:
               print("Invalid input.  I'm just going to take that as a no.")
       
        elif go == 0:	 	 		# Computer turn
           att = random.randint(1,5)            # Determines if zombie attacks 
           super_att = random.randint(1,3)	# Determines the strength of att
           if super_att == 1:
               zomb_a_one = 20.0
           elif super_att == 2:
               zomb_a_one = 2.0 
           else: 
               zomb_a_one = 6.0

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
    global you_hp

    d_intro()
    
    game = True		# Initializes the variable game to True
    while game == True:
        z = random.randint(0,3)		# Randomly decides if player fights zombie
        if z == 3:
            fight()
        check_pos()	# Checks the position of the character
        dev = input("\nwhat are you going to do\n").lower()
     
        # Quits the game
        if dev == "quit": 
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
        # Tells the player respective x and y positions
        elif dev == 'pos x':
            print(pos_x)
        elif dev == 'pos y':
            print(pos_y) 
        # Prints a map base on position
        elif dev == "map":     
            if pos_x <= 2 and pos_y <= 2:
                print(map_base)
                if pos_x == 0 and pos_y == 0:
                    print("you are in the bathroom")
                elif pos_x == 0 and pos_y == 1:
                    print("you are downstairs")
                elif pos_x == 0 and pos_y == 2:
                    print("you are downstairs")
                elif pos_x == 1 and pos_y == 1:
                    print("you are in the bedroom")
                elif pos_x == 1 and pos_y == 2:
                    print("you are upstairs")
                elif pos_x == 1 and pos_y == 3:
                    print("you are upstairs")
                elif pos_x == 2:
                    print("you are outside")
            elif pos_x > 2 and pos_x <= 8 and pos_y == 2:
                print(map_outside)
                if pos_x > 2 and pos_x <= 7 and pos_y == 2:
                    print("you are on the road to the park")
                    if pos_x == 4:
                        print("you are infront of gram's house")
                if pos_x == 8 and pos_y == 2:
                    print("you are in the park")
            else:
                print("no map... you are somewhere? \nTry moving up or down!")
        # Misc commands
        elif dev == "check items": # Displays items in stuffs
            print(stuffs)
        elif dev == "health":	   # Shows how many health points you have
            print(you_hp)
        elif dev == "drink":	   # You want to drink to inrease hp
            have = check_items("water")
            if have == True:
                hp_up = random.randint(2, 5)
                you_hp += hp_up
                stuffs.remove('water')
                print("your hp increased by " + str(hp_up))
            elif have == False:
                print("you don't have any water... sucks your you, I'll just drink this nice water here.")
            else:
                print("something went horrible wrong")
        elif dev == "eat":	   # You want to drink to inrease hp
            have = check_items("food")
            if have == True:
                hp_up = random.randint(4, 7)
                you_hp += hp_up
                stuffs.remove('food')
                print("your hp increased by " + str(hp_up))
            elif have == False:
                print("you don't have any food...")
            else:
                print("something went horrible wrong")
        elif dev == "search":	# Search for stuff
            search()
        elif dev == "drop":	# Drops stuff
            drop() 
        else: 
            print("what is this \"" + dev + "\" nonsense")

# The introduction
print("\n \n \n \nHello and welcome to the game.  It is about you!  Also about zombies.  If this is your first time playing you should type in 'how to play' so that you can learn to play the game.  If you played the game before, took a look at the code before playing or are exceptional at guessing, type in 'start' to begin.") 
opt = input()
if opt == 'start': 
    main()
elif opt == 'how to play':
    print("\n\n\n\nHOW TO PLAY:  \n\nMAIN CONTROLS:  There are several functions you can do in this game.  To move around you simply enter which way you want to go.  For example, if you want to go left, type in \"left\".  It is important to note that your movements are traked using a grid system.  You can find your position in the x or y plane at any time by inputting \"pos x\" or \"pos y\".\nTo print a map so you can know where in the world you are, input \"map\".  It will show you a map and tell you where you are.\nAs you might assume, you are carrying stuff.  To see what you are holding you can input \"check items\".  You can also drop stuff by inputting \"drop\" or check if you can pick anything up from your environment by inputting \"search\".\nIf you want to know how many health points you have, type in \"health\"   \n \nFIGHTING:  You can also fight zombies in this game.  At any one time you can fight one or two zombies but keep in mind, your friend in fat and lazy and does not help you while you fight.  First you will be told how many zombies you are fighting.  Then you can choose to fight by typeing in \"yes\" or you can choose to get away from the fight by typeing in \"run\" and \"no\" to do niether.  To choose which zombie you wish to attack, press \"1\" for zombie one, or \"2\" for zombie two.\nIf your hp is low after fighting some zombies you can eat or drink by typing in \"eat\" or \"drink\".  Remeber that you need to have food or water for you do this... unless you are a wizard then you just need to remeber aquaerupto.  \nThat is it.  Also, sometimes you can kill a zombie into negative hp.  Don't worry about that, you are just that awesome.")
    if input() == 'start':
        main()
    elif input() == 'quit':
       exit 
else:
    print("Sorry, a zombie bit off the part of the code that was suppose to understand that.  HAAAA SHUTING DOWN.")
    
    # TESTING CODE
    # runs the 'check_items' fuction and returns an output based on the stuffs 
    #have = check_items('pliers')
    #if have == True: print("you have that")
    #elif have == False: print("you do not have that")
    #else: print("something went horribly wrong")
##################################################################################
