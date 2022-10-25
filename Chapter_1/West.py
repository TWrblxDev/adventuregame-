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
import items
import items.ammo
import items.food
import items.dollar
import simple_colors
import items.power
import debug.debug
import time
import random
import os
import keyboard
import inv.inv
import items.Battle


items = ['Money', 'Ammo', 'Food', 'Water', 'A Phone']
attacks = ['A Dog', 'A Snake', 'A Bear']
powerups = ['Monster Energy']

dollar = 20
PlayerHealth = 100
EnemyHealth = 20
EnemyDamage = 20
food = 20
dollar = 20
ammo = 10
food = food - 2


clear = lambda: os.system('clear')


def West():
  food = 20
  dollar = 20
  ammo = 10
  food = food - 2
  print("you decided to go West")  
  time.sleep(0.5)
  print("You keep going West")
  clear()
  time.sleep(5)
  print("You find", random.choice(items))
   # ^ Will chose from a list
  print("You are ready to continue walking again")
  time.sleep(2.8)
  clear()
  time.sleep(1)
  print("Walking...")
  time.sleep(5)
  clear()
  print("You come across", random.choice(attacks))
  clear()
  print("Day 1 Is Ending")
  print("Your Stats...")
  print("Food:", food)
  print("$",dollar)
  print("Ammo:", ammo)
  time.sleep(3)
  clear()
  print("Day 2 Rises")
  time.sleep(3)
  clear()
  print("You wake up its 8:30 AM in the morning on Tuesday")
  print('Bill says "Good Morning"')
  print('You Say "Good Morning Bill"')
  west = input("Are you Ready for the day? Yes Or No")

  while not(west == "yes" or "no"):
    print("Please input yes or no")
    if west.lower() == "yes":
      print("Ok Lets go")

      items.Battle.battle()
  
  print("You survuved your first battle. another path leads North and west")
  file = input ("North or west")

  if file.lower() == "north" or "North":
    Chapter_1.North.north()
  elif file.lower() == "west":  
    print("West")


    
    
  
  
  