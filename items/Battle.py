import os 
import time
import Blaster_Pistol
import Game_Time
import keyboard
import sys
import Chapter_1.East
import Chapter_1.North
import Chapter_2.Chapter2
import Chapter_3.Chapter3
import inv.inv
import random
import items.ammo
import items.food
import items.dollar
import simple_colors
import items.power
import items.monster
import debug.debug
import Credits.Credits
import items.Battle
import simple_colors
red = simple_colors.red
yellow = simple_colors.yellow
blue = simple_colors.blue
cyan = simple_colors.cyan
magenta = simple_colors.magenta
green = simple_colors.green
import time
import random

def battle():
  names = "zombie"
  
  
  EnemyHealth = 100
  PlayerHealth = 50
  ClearLoop = 80

  
  
  print("fight starting")
  time.sleep(1)
  print("...")
  time.sleep(1)
  print("ready?")
  time.sleep(1)
  print("fight!")
  time.sleep(1)
  while EnemyHealth > int(0):
    while ClearLoop > int(0):
      print(" ")
      ClearLoop = (ClearLoop - 1)

      if PlayerHealth < int(1):
        print("You Died! Restart The Game To Replay")
        exit()

      
      print("Enemy Health = ", EnemyHealth)
      time.sleep(0.5)
      print("Player Health = ", PlayerHealth)
      time.sleep(0.5)
      print(" ")
      print(
                "type 'attack' to deal damage, type 'heal' to restore health by 30"
            )
      print("mistyping the action will cause you to miss the attack")
      file = input("")

            #Attack
      if file == ("attack" or "Attack"):
        EnemyHealth = (EnemyHealth - 10)
        print(" ")
        print(green("You attacked, and dealt 10 DMG"))
        time.sleep(1)
            #heal
      if file == ("heal" or "Heal"):
        PlayerHealth = (PlayerHealth + 30)
        print(" ")
        print(cyan("You healed yourself for 20 HP"))
        time.sleep(0.5)
           #max health
        if PlayerHealth > int(60):
          PlayerHealth = 60
          print(" ")
          print(red("Max HP reached!"))
          time.sleep(0.5)
            #Enemy attack
      PlayerHealth = (PlayerHealth - 10)
      print(" ")
      print(red("The Enemy attacked you, dealing 10 DMG"))
      file = ("")
      time.sleep(1)
      ClearLoop = 80
        #If you won battle
      if EnemyHealth == 0:
        dollar = 5
        print(" ")
        print("You won the fight!")
        print(" ")
        print("+5 Dollars")
        dollar = dollar + 5
        print("You have $", dollar)

    battle()   #delete this line here temporarily (line 94) to skip battle. if you forgot what goes here. this is the command:   battle()    don't forget indent
