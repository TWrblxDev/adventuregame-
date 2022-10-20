import os 
import time
import Blaster_Pistol
import Game_Time
import keyboard
import sys
import Chapter_1
import Chapter_1.East
import Chapter_1.North
import Chapter_2.Chapter2
import Chapter_3.Chapter3
import inv.inv
import random
import items
import items.ammo
import items.food
import items.dollar
import simple_colors
import items.power
import items.monster
import debug.debug
import Credits.Credits



clear = lambda: os.system('clear')


battle = items.Battle.battle()
#Chapter_1.North.north()
#Chapter_1.Chapter_1.Chapter1()
#Chapter_3.Chapter3.Chapter3()
#Chapter_1.East.East()

#Chapter_2.Chapter2.loaded()
#inv.inv.inv()
exit()
#Make sure to clean up the statements and to add comments, I have no idea what the code is doing

#items.monster.monster()

debug.debug.debug()

original_stdout = sys.stdout




Credits.Credits.credits()

clear()



#simple_colors
red = simple_colors.red
yellow = simple_colors.yellow
blue = simple_colors.blue
cyan = simple_colors.cyan
magenta = simple_colors.magenta
green = simple_colors.green
clear()


print(yellow("Welcome"), blue("To the"), red("adventure Game"))
file = input(yellow("Continue or start a new game? "))

clear()



time.sleep(5)

clear()

if file == "Continue" or "continue":
    print(red("there is no saved game!"))
    file = input(yellow("Start a new game?"))
    if file == "start" or "Start" or "yes" or "Yes":
        print("")
        print(red("IMPORTANT - when typing something, use lowercase"))
        #inv.inv.inv()
        time.sleep(3)
        clear()
        time.sleep(1)
        
       
        print(blue("Loading."))
        time.sleep(1)
        clear()
        print(cyan("Loading.."))
        time.sleep(1)
        clear()
        print(red("Loading..."))
        time.sleep(1)
        clear()
        
        time.sleep(1)
        clear()
        time.sleep(1)
        print(yellow("Loaded"))
        time.sleep(1)
        clear()
        print(cyan("Adventure Game"))
        print(red("A game by"))
        print(yellow("By James and Michael"))
        print(blue("Have fun"))
        print(magenta("A personal project by us and others"))
        print(blue("2022"))
        time.sleep(5)
        clear()
        print(yellow("Are you ready?"))
        file = input(" To Play: ")
        if file == "yes" or "Yes":
            clear()
            NAME = str(input(blue("Enter your name for the game: ")))
            print("hello", NAME, "I am Your Guide for your adventure. You can call me Bill")
            time.sleep(2)
            print("Starting game...")
            clear()
            print("Starting game...")
            clear()
            input(
                "You wake up in a nice cozy bed. You look around and see a bunch of cloths on the floor. You walk over to your radio and turn it on. "
            )
            
            clear()
            input(blue('On the radio, "Good Morning Canada" the announcer says'))
            input(
                "We interupt this program for breaking news!! Zombies have attacked eastern Canada and on on the move to Ontario. If you are near these area we urge you to ready yourselfs. "
            )
            print("")
            print("")
            print("")
            print("")
            input(red('You say "OH NO. I better get ready for battle."'))
            clear()
            time.sleep(1)
            #This part is for the weapon of choice
            print(blue('Choose your Weapon', ["blink", "reverse"]))
            print("")

            file = input(blue("Your Weapon is Blaster Pistol. Type 'ok' to continue"))

            if file == "ok" or "Ok" or "OK":
                Blaster_Pistol.loaded()
            
#I think the best way to solve the problem with the weapons is to make it so you get to buy them later
#

              

