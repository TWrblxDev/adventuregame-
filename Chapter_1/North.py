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
missingitem = 'Your Phone'

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
  print("You Wake up to", simple_colors.red (missingitem),(" Missing"))
  print("You say", simple_colors.red('"OH NO!"'))

  