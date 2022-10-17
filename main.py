import os 
import time
import Blaster_Pistol
import Game_Time
import keyboard
import sys
import Chapter_1.East
import Chapter_1.North
import Chapter_2.Chapter2
import inv.inv
import random
import items.ammo
import items.food
import items.dollar

clear = lambda: os.system('clear')


#Chapter_1.North.north()
#Chapter_1.East.East()
#Chapter_2.Chapter2.loaded()
#inv.inv.inv()
#exit()
#Make sure to clean up the statements and to add comments, I have no idea what the code is doing

original_stdout = sys.stdout



time.sleep(5)
clear()

#Skips intro
#Chapter_1.Chapter_1.Chapter1()
#exit()





print("Welcome to this adventure game.")
file = input("Continue or start a new game? ")

if file == "Continue" or "continue":
    print("there is no saved game!")
    file = input("Start a new game?")
    if file == "start" or "Start" or "yes" or "Yes":
        print("IMPORTANT - when typing something, use lowercase")
        inv.inv.inv()
        time.sleep(3)
        clear()
        time.sleep(1)
        print("Loading...")
        time.sleep(1)
        clear()
        time.sleep(1.02)
        print("Loaded")
        time.sleep(1.999999999999999999999999999)
        clear()
        print("Adventure Game")
        print("A game by")
        print("By James and Michael")
        print("Have fun")
        print("A personal project by us")
        print("2022")
        time.sleep(1)
        clear()
        print("Are you ready?")
        file = input(" To Play: ")
        if file == "yes" or "Yes":
            clear()
            NAME = str(input("Enter your name for the game: "))
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
            input('On the radio, "Good Morning Canada" the announcer says')
            input(
                "We interupt this program for breaking news!! Zombies have attacked eastern Canada and on on the move to Ontario. If you are near these area we urge you to ready yourselfs. "
            )
            
            input('You say "OH NO. I better get ready for battle."')
            clear()
            time.sleep(1)
            #This part is for the weapon of choice
            print('Chose your Weapon')
            print("")

            file = input("Your Weapon is Blaster Pistol. Type 'ok' to continue ")

            if file == "ok" or "Ok" or "OK":
                Blaster_Pistol.loaded()
            
#I think the best way to solve the problem with the weapons is to make it so you get to buy them later


              
                        
