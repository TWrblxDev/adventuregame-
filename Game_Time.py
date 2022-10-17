import time
import os
import Chapter_1.Chapter_1
#after this we should work on this during lunch so we can talk to each other
#you can have and are encouraged to use more than one function.
#it makes it easier to read the code and easier for you to diagnose and solve bugs
def game():
  print("Game is Getting Ready")
  time.sleep(1)
  file = input('Game Starting type "Ok" to continue ')
  if file == "Ok" or "ok":
    print("working")
    clear = lambda: os.system('clear')
    maxhealth = 100
    hp = 100
    print("Your Health: {}".format(hp))
    time.sleep(1)
    print("Working")
    print("Loading.")
    time.sleep(0.5)
    clear()
    print("Loading..")
    time.sleep(0.5)
    clear()
    print("Loading...")
    clear()
    Chapter_1.Chapter_1.Chapter1()