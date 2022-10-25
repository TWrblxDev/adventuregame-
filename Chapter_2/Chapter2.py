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

clear = lambda: os.system('clear')

def loaded():
  print("[DEBUG] - Loaded Chapter 2")
  clear()
  print(simple_colors.blue("Chapter 2"))
  print("TIP: when you start a game. type Chapter 2 and chapter 2 will load.")
  