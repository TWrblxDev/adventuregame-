import time
import Game_Time
import simple_colors

def loaded():
  print(simple_colors.cyan("Blaster Pistol Selected"))
  time.sleep(1)
  print('Ready for War')
  Game_Time.game()