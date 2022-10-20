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
import os
import food
import ammo
import simple_colors
import items.Battle
import random

1 == "Your Water"
2 == "Your Food"
3 == "Your Flashlight"
4 == "Your Backpack"
5 == "Your Phone"

red = simple_colors.red
yellow = simple_colors.yellow
blue = simple_colors.blue
cyan = simple_colors.cyan
magenta = simple_colors.magenta
green = simple_colors.green


clear = lambda: os.system('clear')

def north():
  print("You decide to go North")
  input("you are walking from some time now going North for 6 hours. depleteing you of all of your energy, but you finally arrive in Quebec City ")
  input("you go to the inn and buy a room for $5")
  dollar = 10
  dollar = dollar - 5
  print("$",dollar)
  
 
  print("Your Stats...")
  print("Food:", food)
  print("$", dollar)
  print("Ammo:", ammo)
  i = 3
  while i > 0:
        print("Day 2 rising.")
        time.sleep(1)
        clear()
        print("Day 2 rising..")
        time.sleep(1)
        clear()
        print("Day 2 rising...")
        time.sleep(1)
        clear()
        i = i - 1
  print("Day 2 has rosen")
  print("Welcome", simple_colors.green("To Day 2"))
  
  missing = random.randint(1,5)
  if missing == 1:
    print(red("Your missing your Water bottle"))
  if missing == 2:    
    print(red("Your missing your your rations"))
  if missing == 3:
    print(red("Your missing your backpack"))
  if missing == 4:
    print("Your Missing your Flashlight")
  if missing == 5:
    print("Your Missing Your Phone")

 
  
  print("You say", simple_colors.red('"OH NO!"'))
  print("you say'maybe an enemy took it'")
  items.Battle.battle()
  print("Bill says 'look the zombie dropped something'")
  print("You say ' Hey look it's my item'")
  print("")
  clear()
  print(red("Chapter 1 ending..."))
  print(red("Chapter 2"))
  Chapter_2.Chapter2.loaded()