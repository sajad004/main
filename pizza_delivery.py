print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0 

if size == "S" :
  bill = 15 
  desc = "Small"
if size == "M" :
  bill = 20 
  desc = "Medium"
if size == "L":
  bill = 25 
  desc = "Large"
if add_pepperoni == "Y" :
  if size == "M" :
    bill += 2
  else :
    bill += 3
  desc += " with pepperoni"
if extra_cheese == "Y" :
  bill += 1
  desc += "and extra cheese"

confirm = input(f"Confirm order: {desc} pizza for {bill}$. Y or N ")
if confirm == "Y":
  print (f"Your order: {desc} pizza")
  print (f"Total bill: {bill}$")
else:
  print("Order cancelled.")
