import items.ammo
import items.food
import items.dollar


food = items.food.food

def inv():
  print("[DEBUG] - Loaded Inv")
  file = input("Say Inv or inv to view your inventory at any time")
  if file == "Inv" or "inv":
    print("Inv")
    items.food.food()