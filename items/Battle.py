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
black = simple_colors.black
import time
import random
clear = lambda: os.system('clear')



def battle():
  
  

  
  
  PlayerHealth = 50
  ClearLoop = 80

  
  1 == "Zombie"
  2 == "Huge Zombie"
  3 == "Mutated Huge Zombie"
  4 == "Mutated Monster Fish"
  5 == "Mutated Monster Spider"

  enemy = random.randint(1,5)
  if enemy == 1:
    EnemyHealth = random.randint(90,110)
    print("You are fighting a zombie")
  if enemy == 2:
    EnemyHealth = random.randint(110, 130)
    print("You are fighting a Huge Zombie")
  if enemy == 3:
    EnemyHealth = random.randint(130, 160)
    print("You are fighting a Huge Mutated Zombie")
  if enemy == 4:
    EnemyHealth = random.randint(90,150)
    print("You are fighting a Mutated Monster Fish")
  if enemy == 5:
    EnemyHealth = random.randint(90,200)
    print("You are fighting a Mutated Monster Spider")

    
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
                "type 'attack' to deal damage, type 'heal' to restore health by 20"
            )
      print("mistyping the action will cause you to miss the attack")
      file = input("")

            #Attack
      if file == ("attack" or "Attack"):
        EnemyHealth = (EnemyHealth - 10)
        print(" ")
        print(green("You attacked, and dealt 10 DMG"))
        #Cheat
        time.sleep(1)
      if file == ("die"):
        EnemyHealth = 0
            #heal
      if file == ("heal" or "Heal"):
        PlayerHealth = (PlayerHealth + 20)
        print(" ")
        print(cyan("You healed yourself for 20 HP, but the zombie will attack."))
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
      print(red("The enemy attacked you dealing 10 DMG"))
      
      time.sleep(1)
      clear()
      ClearLoop = 80
        #If you won battle
      if EnemyHealth == 0:
        dollar = 5
        print(" ")
        print(magenta("You won the fight!", ['bright']))
        print(" ")
        print(cyan("+5 Dollars"))
        dollar = dollar + 5
        print("You have $", dollar)
      break
     #delete this line here temporarily (line 94) to skip battle. if you forgot what goes here. this is the command:   battle()    don't forget indent
