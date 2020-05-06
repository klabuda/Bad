#!/usr/bin/python
#channelwood.py: A text adventure game based on the video game Myst

#############################################################################
#                                                                           #
#       Disclaimer: This game is based on the 1993 game Myst designed       #
#                   by Robyn and Rand Miller and developed by Cyan, Inc.    #
#                   This adventure is a tribute to their amazing game       #
#                   am in no way profiting from it.                         #
#                   If anyone is interested in finding out more about       #
#                   Myst, please visit Cyan, Inc.'s website:                #
#                   https://cyan.com/games/myst/                            #
#                                                                           #
#############################################################################

########## IMPORTS ##########

import time

########## END OF IMPORTS ##########


########## SWITCH CLASS ##########

class Switch(object):

    def __init__(self,state):
        self.setState(state) # sets the default blocked state

    def getState(self):
        return self._state # returns the state of the switch

    def setState(self,state):
        self._state = state # sets a new state

    def __eq__(self,state):
	return self.getState() == state # returns if string equals state

########## END OF SWITCH CLASS ##########


########## WORLD CLASS ##########

class World(object):
	# default states for items, switches, pump, pipe, elevator, doors, and walkways
    _red = False
    _blue = False
    _book = False
    _switch01 = Switch("South")
    _switch02 = Switch("South")
    _switch03 = Switch("West")
    _switch06 = Switch("East")
    _switch07 = Switch("South")
    _switch10 = Switch("East")
    _pump09 = False
    _pipe40 = False
    _elev05 = True
    _door08 = False
    _door26 = False
    _walk13 = False    


##### INITIALIZE #####
    def __init__(self): # prints a welcome statement and goes to Room 00
		
        print("\n"*5)
        print('''Welcome to Channelwood, a text adventure game based on the 1993 game, Myst. Myst was designed by Robyn and
Rand Miller and developed by Cyan, Inc. You can find out more about this amazing game here:
https://cyan.com/games/myst/

It is advised to make a map while playing this game. Everything is laid out in a grid. Enjoy!

.
.
.
.
.

You are riding an elevator down into an underground chamber. Once you come to a stop you step out into a dark
room. On a table in front of you, you see a book with "Channelwood" written in elegant script on the cover.
You know you'll be able to find another red and blue page in this age to learn more about Sirrus and Achenar.
You open the book and press your hand to the window in the page. Everything goes black.

You emerge in a new age. You immediately hear a cacophony of birds, frogs, and insects and an underlining
calming lapping of water on wood. You are standing with your back to a tree so tall you can't see the top and
more trees just as tall are all around you. You are standing on a wooden walkway that is just above the water's
surface.''')
        self.room00()


##### GET PLAYER CHOICE #####
    def getChoice(self,options):
        
        choice = raw_input("\nEnter choice: ") # asks for input
        
        while choice not in options: # compares input to option list and asks again if it doesn't exist
            choice = raw_input("Please enter a valid choice (ex. 1): ")

        return choice # returns the corrected input


##### GOALS #####
    def goals(self):
        print("\n")
        print("*"*50)
        print("\nGoals:")
        if not self._red:
            print("Find the red page") # prints if player has not found the red page
        if not self._blue:
            print("Find the blue page") # prints if the player has not found the blue page
        if not self._book:
            print("Find the Myst linking book") # prints if the player has not found the linking book
        print("Return to Myst\n") # end goal
        print("*"*50)


##### ELEVATOR 05 #####
# The elevator in Room 05 is powered if the following conditions are met
    def elevator05(self):
	return self._pump09 and self._switch02 == "East" and self._switch03 == "South" and self._switch06 == "North" and self._switch07 == "South"


##### ELEVATOR 26 #####
# The elevator in Room 26 is powered if the following conditions are met
    def elevator26(self):
	return self._pump09 and self._switch07 == "East"


##### ELEVATOR 39 #####
# The elevator in Room 39 is powered if the following conditions are met
    def elevator39(self):
	return self._pump09 and self._switch02 == "East" and self._switch03 == "West" and self._switch06 == "North" and self._switch07 == "South"


##### WALKWAY 13 #####
# The walkway generator in Room 13 is powered if the following conditions are met
    def walkway13(self):
	return self._pump09 and self._switch07 == "South" and (self._switch06 == "East" and self._switch10 == "North" or self._switch01 == "South" and self._switch02 == "South" and self._switch06 == "North")


##### ROOM 00 #####
# The starting room
    def room00(self):
        options = ["1","2"] # each room has a list of valid options
        
        print("\n")
        print('''There is a pipe on the side of the walkway. One end disappears into the water and the other continues on 
the walkway. The walkway ends at the base of a tree and extends to the north.

What do you do?
	1) Go North
	2) Review goals''') # each room prints out a room state and available options
        
        player_choice = self.getChoice(options) # get player input

        if player_choice == "1": # decide where to go based on player input
            self.room01()
        else:
           self.goals()
           self.room00()


##### ROOM 01 #####
    def room01(self):
        options = ["1","2","3","4","5","6"]
        
        print("\n")
        print('''The walkway branches off in three directions to the North, South, and West. The pipe continues along each of 
these branches. At your feet, you see a switch. The switch currently indicates the pipe is blocked off to the 
''' + self._switch01.getState() + '''

What do you do?
	1) Change the switch to block off the pipe to the North
	2) Change the switch to block off the pipe to the South
	3) Go North
	4) Go South
	5) Go West
	6) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self._switch01.setState("North") # changes state of the switch
            self.room01()
        elif player_choice == "2":
            self._switch01.setState("South")
            self.room01()
        elif player_choice == "3":
            self.room14()
        elif player_choice == "4":
            self.room00()
        elif player_choice == "5":
            self.room02()
        else:
           self.goals()
           self.room01()


##### ROOM 02 #####
    def room02(self):
        options = ["1","2","3","4","5","6"]

	print("\n")
        print('''The walkway branches off in three directions to the East, South, and West. The pipe continues along each of 
these branches. At your feet, you see a switch. The switch currently indicates the pipe is blocked off to the 
''' + self._switch02.getState() + '''

What do you do?
	1) Change the switch to block off the pipe to the East
	2) Change the switch to block off the pipe to the South
	3) Go East
	4) Go South
	5) Go West
	6) Review goals''')

        player_choice = self.getChoice(options)

	if player_choice == "1":
            self._switch02.setState("East") # changes the state of the switch
            self.room02()
        elif player_choice == "2":
            self._switch02.setState("South")
            self.room02()
        elif player_choice == "3":
	    self.room01()
        elif player_choice == "4":
            self.room03()
        elif player_choice == "5":
            self.room06()
        else:
            self.goals()
            self.room02()


##### ROOM 03 #####
    def room03(self):
        options = ["1","2","3","4","5","6"]

        print("\n")
        print('''The walkway branches off in three directions to the North, South, and West. The pipe continues along each of 
these branches. At your feet, you see a switch. The switch currently indicates the pipe is blocked off to the 
''' + self._switch03.getState() + '''

What do you do?
	1) Change the switch to block off the pipe to the South
	2) Change the switch to block off the pipe to the West
	3) Go North
	4) Go South
	5) Go West
	6) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self._switch03.setState("South") # changes the state of the switch
            self.room03()
        elif player_choice == "2":
            self._switch03.setState("West")
            self.room03()
        elif player_choice == "3":
            self.room02()
        elif player_choice == "4": # will go to Room 04a or 04b depending on the state of the pipe
            if self._pipe40:
                self.room04b()
            else:
                self.room04a()
        elif player_choice == "5": # will go to Room 05a or 05b depending on the state of the elevator
            if self._elev05:
                self.room05a()
            else:
                self.room05b()
        else:
            self.goals()
            self.room03()


##### ROOM 04a #####
# Room 4 with pipe retracted
    def room04a(self):
        options = ["1","2"]

        print("\n")
        print('''You reach a dead end. The walkway and pipe end abruptly. across the water you can see both the pipe and
walkway continue. On that walkway is a wheel which looks like it will extend the pipe

What do you do?
	1) Go North
	2) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room03()
        else:
            self.goals()
            self.room04a()


##### ROOM 04b #####
# Room 4 with pipe extended
    def room04b(self):
        options = ["1","2"]

        print("\n")
        print('''You reach a dead end. The walkway end abruptly, but the pipe continues on accross a gap. You can see it
running along another walkway on the other side.

What do you do?
	1) Go North
	2) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room03()
        else:
            self.goals()
            self.room04b()


##### ROOM 05a #####
# Room 5 with elevator down
    def room05a(self):
        options = ["1","2","3"]

        print("\n")
        print('''In front of you is a wooden elevator that is suspended on a pulley system from a tree branch above. Inside the
elevator is a switch. On the walkway in front of the elevator is a generator that is connected to the pipe.

What do you do?
	1) Press switch
	2) Go East
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            if self.elevator05():
                print("\nYou ride the elevator up into the trees. You exit the elevator onto a wooden platform. You look up and still can't see\n\
the tops.")
                self._elev05 = False # changes the state of the elevator to be up
                self.room15a()
            else:
                print("\nNothing happens. You need to find some way to power the elevator.")
                self.room05a()
        elif player_choice == "2":
            self.room03()
        else:
            self.goals()
            self.room05a()


##### ROOM 05b #####
# Room 5 with elevator up
    def room05b(self):
        options = ["1","2"]

        print("\n")        
        print('''You reach a dead end. The elevator is no longer here. on the walkway in front of you is a generator that 
is connected to the pipe.

What do you do?
        1) Go East
        2) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room03()
        else:
            self.goals()
            self.room05b()


##### ROOM 06 #####
    def room06(self):
        options = ["1","2","3","4","5","6"]

        print("\n")
        print('''The walkway branches off in three directions to the North, East, and West. The pipe continues along each of 
these branches. At your feet, you see a switch. The switch currently indicates the pipe is blocked off to the 
''' + self._switch06.getState() + '''

What do you do?
	1) Change the switch to block off the pipe to the North
	2) Change the switch to block off the pipe to the East
	3) Go North
	4) Go East
	5) Go West
	6) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self._switch06.setState("North")
            self.room06()
        elif player_choice == "2":
            self._switch06.setState("East")
            self.room06()
        elif player_choice == "3":
            self.room10()
        elif player_choice == "4":
            self.room02()
        elif player_choice == "5":
            self.room07()
        else:
            self.goals()
            self.room06()


##### ROOM 07 #####
    def room07(self):
        options = ["1","2","3","4","5","6"]

        print("\n")
        print('''The walkway branches off in three directions to the North, East, and South. The pipe continues along each of 
these branches. At your feet, you see a switch. The switch currently indicates the pipe is blocked off to the
''' + self._switch07.getState() + '''

What do you do?
	1) Change the switch to block off the pipe to the East
	2) Change the switch to block off the pipe to the South
	3) Go North
	4) Go East
	5) Go South
	6) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self._switch07.setState("East")
            self.room07()
        elif player_choice == "2":
            self._switch07.setState("South")
            self.room07()
        elif player_choice == "3":
            self.room09()
        elif player_choice == "4":
            self.room06()
        elif player_choice == "5":
            self.room08()
        else:
            self.goals()
            self.room07()


##### ROOM 08 #####
    def room08(self):
        options = ["1","2","3"]

        print("\n")
        print('''In front of you is a wooden staircase that goes up around the trunk of a tree. In front of the staircase is a
door. In front of the door is a generator that is connected to the pipe. There is a steel cable going from the 
generator into the branches above.

What do you do?
	1) Open door
	2) Go North
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            if self._door08: # check status of door08
                print("\nYou open the door and go up the staircase.")
                self.room26()
            else:
                print("\nThe door is locked.")
                self.room08()
        elif player_choice == "2":
            self.room07()
        else:
            self.goals()
            self.room08()


##### ROOM 09 #####
    def room09(self):
        options = ["1","2","3"]

        print("\n")
        print('''The walkway ends at a small island. The pipe here is connected to a hose that follows a sandy path up into a 
small wooden hut. Inside the hut you find a water water pump that is connected to the hose. At the base of the
pump is a valve. ''')
        if self._pump09: # checks state up pump and prints
            print("The valve is currently in the on position")
        else:
            print("The valve is currently in the off position")

        print('''   
What do you do?
	1) Turn valve
	2) Go south
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            if self._pump09:
                print("\nYou turn the valve to the off position. The sound of running water stops.")
                self._pump09 = False
                self.room09()
            else:
                print("\nYou turn the valve to the on position. You hear water rush into the hose.")
                self._pump09 = True
                self.room09()
        elif player_choice == "2":
            self.room07()
        else:
            self.goals()
            self.room09()


##### ROOM 10 #####
    def room10(self):
        options = ["1","2","3","4","5","6"]

        print("\n")
        print('''The walkway branches off in three directions to the North, East, and South. The pipe continues along each of 
these branches. At your feet, you see a switch. The switch currently indicates the pipe is blocked off to the
''' + self._switch10.getState() + '''

What do you do?
	1) Change the switch to block off the pipe to the North
	2) Change the switch to block off the pipe to the East
	3) Go North
	4) Go East
	5) Go South
	6) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self._switch10.setState("North")
            self.room10()
        elif player_choice == "2":
            self._switch10.setState("East")
            self.room10()
        elif player_choice == "3":
            self.room11()
        elif player_choice == "4":
            self.room12()
        elif player_choice == "5":
            self.room06()
        else:
            self.goals()
            self.room10()


##### ROOM 11 #####
    def room11(self):
        options = ["1","2"]

        print("\n")
        print('''You reach a dead end. The walkway and pipe here are destroyed. It looks like a tree fell on it.

What do you do?
	1) Go South
	2) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room10()
        else:
            self.goals()
            self.room11()


##### ROOM 12 #####
    def room12(self):
        options = ["1","2","3","4"]

        print("\n")
        print('''The walkway branches off in three directions to the North, East, and West. The pipe continues along each of 
these branches.

What do you do?
	1) Go North
	2) Go East
	3) Go West
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            if self._walk13:
                self.room13b()
            else:
                self.room13a()
        elif player_choice == "2":
            self.room14()
        elif player_choice == "3":
            self.room10()
        else:
            self.goals()
            self.room12()


##### ROOM 13a #####
# Room 13 with walkway lowered
    def room13a(self):
        options = ["1","2","3"]	

        print("\n")
        print('''You reach a dead end. On the walkway in front of you is a generator that is connected to the pipe. There is
a lever on the generator.

What do you do?
	1) Pull the lever
	2) Go South
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            if self.walkway13():
                print("\nYou pull the lever and a walkway raises up out of the water to the East")
	        self._walk13 = True
                self.room13b()
            else:
                print("\nNothing happens. You need to find some way to power the generator")
                self.room13a()
        elif player_choice == "2":
            self.room12()
        else:
            self.goals()
            self.room13a()


##### ROOM 13b #####
# Room 13 with walkway raised
    def room13b(self):
        options = ["1","2","3","4"]	

        print("\nROOM13b")
        print('''The walkway branches off in two directions to the East and South. The pipe only continues along the South
path. On the walkway in front of you is a generator that is connected to the end of the pipe. There is a 
lever on the generator.

What do you do?
	1) Pull the lever
	2) Go East
        3) Go South
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            if self.walkway13():
                print("\nYou pull the lever and the Eastern walkway sinks back into the water.")
	        self._walk13 = False
                self.room13a()
            else:
                print("\nNothing happens. You need to find some way to power the generator")
                self.room13b()
        elif player_choice == "2":
            self.room33()
        elif player_choice == "3":
            self.room12()
        else:
            self.goals()
            self.room13b()


##### ROOM 14 #####
    def room14(self):
        options = ["1","2","3"]

        print("\nROOM14")
        print('''The walkway branches off in two directions to the South and to the West. The pipe continues along each of 
these branches.

What do you do?
	1) Go South
	2) Go West
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room01()
        elif player_choice == "2":
            self.room12()
        else:
            self.goals()
            self.room14()


##### ROOM 15a #####
# Room 15 with elevator up
    def room15a(self):
        options = ["1","2","3"]

        print("\n")
        print('''A wooden bridge spans the gap between the platform you are standing on and the next tree to the North. 
Behind you is a wooden elevator. Inside the elevator is a switch.

What do you do?
	1) Press switch
	2) Go North
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            print("\nYou press the switch and desend in the elevator.")
            self._elev05 = True
            self.room05a()
        elif player_choice == "2":
            self.room16()
        else:
            self.goals()
            self.room15a()


##### ROOM 15b #####
# Room 15 with elevator down
    def room15b(self):
        options = ["1","2"]

        print("\nROOM15B")
        print('''You reach a dead end. A wooden bridge spans the gap between the platform you are standing on and the 
next tree to the North.

What do you do?
	1) Go North
	2) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room16()
        else:
            self.goals()
            self.room15b()


##### ROOM 16 #####
    def room16(self):
        options = ["1","2","3","4"]

        print("\nROOM16")
        print('''You are in a small wooden treehouse. There are three bridges leaving the house to the East, South, and West.

What do you do?
	1) Go East
	2) Go South
	3) Go West
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room18()
        elif player_choice == "2":
            if self._elev05:
                self.room15b()
            else:
                self.room15a()
        elif player_choice == "3":
            self.room17()
        else:
            self.goals()
            self.room16()


##### ROOM 17 #####
    def room17(self):
        options = ["1","2"]

        print("\nROOM17")
        print('''You have reached a dead end. You are in a small wooden treehouse. A bridge goes away from the house to the 
East.

What do you do?
	1) Go East
	2) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room16()
        else:
            self.goals()
            self.room17()


##### ROOM 18 #####
    def room18(self):
        options = ["1","2","3"]

        print("\n")
        print('''You are in a large wooden treehouse. There are broken pieces of furniture scattered around. You can see two
bridges leaving the house to the South and to the West.

What do you do?
	1) Go South
	2) Go West
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room19()
        elif player_choice == "2":
            self.room16()
        else:
            self.goals()
            self.room18()


##### ROOM 19 #####
    def room19(self):
        options = ["1","2","3","4"]

        print("\n")
        print('''You are in a large wooden treehouse. There are broken pieces of furniture scattered around. You can see 
three bridges leaving the house to the North, East, and South.

What do you do?
	1) Go North
	2) Go East
	3) Go South
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room18()
        elif player_choice == "2":
            self.room20()
        elif player_choice == "3":
            self.room27()
        else:
            self.goals()
            self.room19()


##### ROOM 20 #####
    def room20(self):
        options = ["1","2","3","4"]

        print("\n")
        print('''You are in a small wooden treehouse. There are three bridges leaving the house to the North, East, and West.

What do you do?
	1) Go North
	2) Go East
	3) Go West
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room21()
        elif player_choice == "2":
            self.room24()
        elif player_choice == "3":
            self.room19()
        else:
            self.goals()
            self.room20()


##### ROOM 21 #####
    def room21(self):
        options = ["1","2","3","4"]

        print("\n")
        print('''You are in a large wooden treehouse. There are broken pieces of furniture scattered around. You can see three
bridges leaving the house to the North, East, and South.

What do you do?
	1) Go North
	2) Go East
	3) Go South
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room22()
        elif player_choice == "2":
            self.room23()
        elif player_choice == "3":
            self.room20()
        else:
            self.goals()
            self.room21()


##### ROOM 22 #####
    def room22(self):
        options = ["1","2"]

        print("\n")
        print('''You have reached a dead end. You are in a small wooden treehouse. A bridge goes away from the house to the 
South.

What do you do?
	1) Go South
	2) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room21()
        else:
            self.goals()
            self.room22()


##### ROOM 23 #####
    def room23(self):
        options = ["1","2","3"]

        print("\n")
        print('''You are in a small wooden treehouse. There are two bridges leaving the house to the South and West.

What do you do?
	1) Go South
	2) Go West
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room24()
        elif player_choice == "2":
            self.room21()
        else:
            self.goals()
            self.room23()


##### ROOM 24 #####
    def room24(self):
        options = ["1","2","3","4"]

        print("\n")
        print('''You are in a large wooden treehouse. There are broken pieces of furniture scattered around. You can see three
bridges leaving the house to the North, South, and West.

What do you do?
	1) Go North
	2) Go South
	3) Go West
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room23()
        elif player_choice == "2":
            self.room25()
        elif player_choice == "3":
            self.room20()
        else:
            self.goals()
            self.room24()


##### ROOM 25 #####
    def room25(self):
        options = ["1","2","3"]

        print("\n")
        print('''You are in a large wooden treehouse. There are broken pieces of furniture scattered around. You can see two
bridges leaving the house to the North and West.

What do you do?
	1) Go North
	2) Go West
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room24()
        elif player_choice == "2":
            self.room26()
        else:
            self.goals()
            self.room25()


##### ROOM 26 #####
    def room26(self):
        options = ["1","2","3","4"]

        print("\n")
        print('''In front of you is a wooden staircase that goes down around the trunk of a tree. In front of the staircase is a
door. Next to the staircase is another wooden elevator. Inside the elevator is a switch. A bridge leaves this
platform to the East.

What do you do?
	1) Open door
	2) Press switch
	3) Go East
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            if self._door26:
                print("\nYou open the door and go down the staircase. You unlock the door at the bottom.")
                self._door08 = True
                self.room08()
            else:
                print("\nThe door is locked. You need to find a way to unlock it.")
                self.room26()
        elif player_choice == "2":
            if self.elevator26():
                print("\nYou press the switch and go up in the elevator. You exit the elevator onto a wooden platform in the\n\
trees. You look up and can now finally see the distant tops.")
                self.room29()
            else:
                print("\nNothing happens. You need to find a way to power the elevator.")
                self.room26()
        elif player_choice == "3":
            self.room25()
        else:
            self.goals()
            self.room26()


##### ROOM 27 #####
    def room27(self):
        options = ["1","2","3"]

        print("\nROOM27")
        print('''You are in a small wooden treehouse. There are two bridges leaving the house to the North and South.

What do you do?
	1) Go North
	2) Go South
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room19()
        elif player_choice == "2":
            self.room28()
        else:
            self.goals()
            self.room27()


##### ROOM 28 #####
    def room28(self):
        options = ["1","2","3"]

        print("\n")
        print('''You have reached a dead end. You are in a small wooden treehouse. A bridge goes away from the house to the 
South. In a window facing Northeast, you can see a large staircase. In front of the window is a lever.

What do you do?
	1) Pull lever
	2) Go North
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            print("\nYou pull the lever and hear a distant click.")
            if self._door26:
                self._door26 = False
            else:
                self._door26 = True
            self.room28()
        elif player_choice == "2":
            self.room27()
        else:
            self.goals()
            self.room28()


##### ROOM 29 #####
    def room29(self):
        options = ["1","2","3","4"]

        print("\n")
        print('''A wooden bridge spans the gap between the platform you are standing on and the next tree to the North and
another bridge extends to the South. Behind you is a wooden elevator. Inside the elevator is a switch.

What do you do?
	1) Press switch
	2) Go North
	3) Go South
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            print("\nYou press the switch and go down in the elevator.")
            self.room26()
        elif player_choice == "2":
            self.room30()
        elif player_choice == "3":
            self.room32()
        else:
            self.goals()
            self.room29()


##### ROOM 30 #####
    def room30(self):
        options = ["1","2","3","4"]

        print("\n")
        print('''You are in an eerily decorated cabin. On the walls you see masks and strange sharp looking instruments. On 
the table in front of you is a wicked looking animal trap. This looks like Achenar's handiwork. Two bridges
leave from this place. One to the North and one to the South.

What do you do?
	1) Touch the trap
	2) Go North
	3) Go South
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            print("\nYou cautiously reach for the trap. It snaps shut before you reach it and an image of Achenar's head\n\
appears above it. It says something in a strange language before fading away.")
            self.room30()
        elif player_choice == "2":
            self.room31()
        elif player_choice == "3":
            self.room29()
        else:
            self.goals()
            self.room30()


##### ROOM 31 #####
    def room31(self):
        options = ["1","2","3","4"]

        print("\n")
        print('''This must have been Achenar's bedchamber. You see a bedframe in disrepair and a strange looking device in the 
corner. A bridge leaves this chamber to the South. On a desk behind you is a blue page. 

What do you do?
	1) Take the blue page
	2) Inspect device
	3) Go South
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            if self._blue:
                print("\nYou already have the blue page!")
                self.room31()
            else:
                print("\nYou take the blue page.")
                self._blue = True
                self.room31()
        elif player_choice == "2":
            print("\nYou touch one of the buttons on the machine and it starts to record you. This must be how Achenar created\n\
his message.")
            self.room31()
        elif player_choice == "3":
            self.room30()
        else:
            self.goals()
            self.room31()


##### ROOM 32 #####
    def room32(self):
        options = ["1","2","3","4"]

        print("\n")
        print('''You are in an opulently decorated wooden cabin. The walls have intricate carvings on them all of the
furniture in this room seems to have avoided the destruction the rest of this age has had. There is a wardrobe
next to you and a grand bed is on the far wall. This looks like Sirrus's domain. A bridge leaves this chamber 
to the North. On a desk next to the bed is a red page.

What do you do?
	1) Take the red page
	2) Open wardrobe
	3) Go North
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            if self._red:
                print("\nYou already have the red page!") # You can't take two red pages
                self.room32()
            else:
                print("\nYou take the red page.")
                self._red = True
                self.room32()
        elif player_choice == "2":
            print("You open the wardrobe and find piles of gold coins and a sinister looking dagger. There are glass vials\n\
containing liquids of various colors on the back of the door. You decide to leave it all alone. You close the wardrobe.")
            self.room32()
        elif player_choice == "3":
            self.room29()
        else:
            self.goals()
            self.room32()


##### ROOM 33 #####
    def room33(self):
        options = ["1","2","3"]

        print("\n")
        print('''The walkway branches off in two directions to the East and West.

What do you do?
	1) Go East
	2) Go West
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room34()
        elif player_choice == "2":
            self.room13b()
        else:
            self.goals()
            self.room33()


##### ROOM 34 #####
    def room34(self):
        options = ["1","2","3"]

        print("\n")
        print('''The walkway branches off in two directions to the South and West.

What do you do?
	1) Go South
	2) Go West
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room35()
        elif player_choice == "2":
            self.room33()
        else:
            self.goals()
            self.room34()


##### ROOM 35 #####
    def room35(self):
        options = ["1","2","3"]

        print("\n")
        print('''The walkway branches off in two directions to the North and South.

What do you do?
	1) Go North
	2) Go South
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room34()
        elif player_choice == "2":
            self.room36()
        else:
            self.goals()
            self.room35()


##### ROOM 36 #####
    def room36(self):
        options = ["1","2","3"]

        print("\n")
        print('''The walkway branches off in two directions to the North and South.

What do you do?
	1) Go North
	2) Go South
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room35()
        elif player_choice == "2":
            self.room37()
        else:
            self.goals()
            self.room36()


##### ROOM 37 #####
    def room37(self):
        options = ["1","2","3"]

        print("\n")
        print('''The walkway branches off in two directions to the North and South.

What do you do?
	1) Go North
	2) Go South
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room36()
        elif player_choice == "2":
            self.room38()
        else:
            self.goals()
            self.room37()


##### ROOM 38 #####
    def room38(self):
        options = ["1","2","3","4"]

        print("\n")
        print('''The walkway branches off in three directions to the North, East, and West. The pipe continues from the
West to the East.

What do you do?
	1) Go North
	2) Go East
	3) Go West
	4) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            self.room37()
        elif player_choice == "2":
            self.room39()
        elif player_choice == "3":
            if self._pipe40: # If pipe is extended go to Room 40b
                self.room40b()
            else: # If pipe is not extended go to Room 40a
                self.room40a()
        else:
            self.goals()
            self.room38()


##### ROOM 39 #####
    def room39(self):
        options = ["1","2","3"]

        print("\n")
        print('''In front of you is a wooden elevator that is suspended on a pulley system from a tree branch above. Inside the
elevator is a switch. On the walkway in front of the elevator is a generator that is connected to the pipe.
The walkway extends out to the West.

What do you do?
	1) Press switch
	2) Go West
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            if self.elevator39(): # The elevator is powered
                print("\nYou go up through the trees, higher than you've been before. Once you reach the top, you step out into \n\
a small dark room.")
                self._book = True # Player has found the Myst linking book
                self.room41()
            else:
                print("\nNothing happens. You need to find a way to power the elevator.") # The elevator is not powered
                self.room39()
        elif player_choice == "2":
            self.room38()
        else:
            self.goals()
            self.room39()


##### ROOM 40a #####
# Room 40 with the pipe retracted
    def room40a(self):
        options = ["1","2","3"]

        print("\n")
        print('''You reach a dead end. The walkway and pipe end abruptly. At the end of the pipe, you see a wheel.

What do you do?
	1) Turn wheel
	2) Go East
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            print("You turn the wheel and the pipe extends to connect on the other side.")
            self._pipe40 = True # pipe is connected to Room 04
            self.room40b()
        elif player_choice == "2":
            self.room38()
        else:
            self.goals()
            self.room40a()

##### ROOM 40b #####
# Room 40 with the pipe extended
    def room40b(self):
        options = ["1","2","3"]

        print("\n")
        print('''You reach a dead end. The walkway ends abruptly, but the pipe continues accross the gap. On the pipe, you see 
a wheel.

What do you do?
	1) Turn wheel
	2) Go East
	3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            print("You turn the wheel and the pipe retracts.")
            self._pipe40 = False # pipe is disconnected from Room 04
            self.room40a()
        elif player_choice == "2":
            self.room38()
        else:
            self.goals()
            self.room40b()


##### ROOM 41 #####
    def room41(self):
        options = ["1","2","3"]

        print("\n")
        print('''Inside this room on a desk is a book with 'Myst' written in bold letters on the cover. Behind you is
the elevator. Inside the elevator is a switch.

What do you do?
	1) Open book
	2) Press switch
        3) Review goals''')

        player_choice = self.getChoice(options)

        if player_choice == "1":
            if self._red and self._blue: # if player has both the red and blue pages, they can continue
                self.room42()
            else:
                print("\nYou need the red and blue pages before you return to Myst.")
                self.room41()
        elif player_choice == "2":
            self.room39()
        else:
            self.goals()
            self.room41()


##### ROOM 42 #####
# The final room
    def room42(self):
        print("\n")
        print('''Congratulations! You've made it back to Myst. Now you need to return the red and blue pages to their books and 
figure out what is going on. Who are Atrus and Catherine? Why are Sirrus and Achenar in prison? Who is 
responsible for burning the library? The adventure continues on Myst.

https://cyan.com/games/myst/''')
        time.sleep(5) # waits for 5 seconds before returning to main

########## END OF WORLD CLASS ##########


########## MAIN ##########

if __name__ == "__main__":

    newGame = "Y"

    while newGame == "Y": # will ask the player if they want to start a new game when they are finished
        game = World()
        print("\n"*50)
        print("Congratulations on fininshing the game!")
        newGame = raw_input("Would you like to play again (Y/N): ").upper()

########## END OF MAIN ##########
