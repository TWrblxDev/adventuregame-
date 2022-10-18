import items.ammo
import items.food
import items.dollar
import simple_colors

food = items.food.food

def inv():
  print(simple_colors.red("[DEBUG] - Loaded Inventory"))
  file = input("Say Inv or inv to view your inventory at any time")
  if file == "Inv" or "inv":
    print("Inv")
    items.food.food()