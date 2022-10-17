import time
import Chapter_1.East
import Chapter_1.West
import Chapter_1.North

time.sleep(0.5)
def Chapter1():
  ch1 = input("you leave your house after getting prepared and grab all of your belonings important  for fighting and surviving.")
  ch1 = input("you have 20 food, $20, and 10 ammo")
  ch1 = input("You walk along the path until you find a fork in the road. ")
  ammo = 10
  print("Ammo:", ammo)
  food = 20
  print("Food:", food)
  Dollar = 20
  print("$",Dollar)
  ch1 = input("Bill 'You can go East, West and North' Type East for East or West for West and north for North") 
  if ch1.lower() == "east":
    Chapter_1.East.East()
  elif ch1.lower() == "west":  
    Chapter_1.West.West()
  elif ch1.lower() == "north":
    Chapter_1.North.north()

