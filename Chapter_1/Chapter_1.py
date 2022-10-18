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
import simple_colors
import items.power
import debug.debug
import time
import Chapter_1.East
import Chapter_1.West
import Chapter_1.North
import simple_colors


#Simple Colors
red = simple_colors.red
yellow = simple_colors.yellow
blue = simple_colors.blue
cyan = simple_colors.cyan
magenta = simple_colors.magenta
green = simple_colors.green

time.sleep(0.5)
def Chapter1():
  ch1 = input("you leave your house after getting prepared and grab all of your belonings important  for fighting and surviving.")
  #ch1 = input("you have, 20 food, $20, and 10 ammo")
  ch1 = input("You walk along the path until you find a fork in the road. ")
  ammo = 10
  print("Ammo:", ammo)
  food = 20
  print("Food:", food)
  Dollar = 20
  print(cyan("$"),Dollar)
  ch1 = input("Bill 'You can go East, West and North' Type East for East or West for West and north for North") 
  if ch1.lower() == "east":
    Chapter_1.East.East()
  elif ch1.lower() == "west":  
    Chapter_1.West.West()
  elif ch1.lower() == "north":
    Chapter_1.North.north()

