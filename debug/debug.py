import inv.inv
import items.ammo
import items.food
import items.dollar
import items.power
import items.monster
import simple_colors

def debug():
  items.power.power()
  items.food.food()
  items.dollar.dollar()
  inv.inv.inv()
  items.monster.monster()

  print(simple_colors.red("Loaded All Files"))
  