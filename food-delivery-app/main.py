veg_menu = ("""
_______________________VEG-MENU_______________________
 ITEM-NUMBER | ITEM NAME
	1				Pizza
	2				Sandwitch
	3				Pav Bhaji
	4 				Veg-Biriyani
	5				Thali 
""")

nonveg_menu = ("""
_______________________NONVEG-MENU_______________________
 ITEM-NUMBER | ITEM NAME
	1				Non-Pizza
	2				Chicken Sandwitch
	3				Fish
	4 				Clicken-Biriyani
	5				Nonveg-Thali 
""")


# EXECUTING CODE


print("""
--------------------WELCOME TO FOOD APP"------------------

THE BEST PLACE TO HAVE DELICIOUS FOOD			
""")

user_name = input("Enter your name: ")

print(f"Welcome {user_name}! We know you are hungry! Pick a dish and we deliver it to you ASAP.")
print()
food_type = int(input("Press 1 for veg, 2 for non-veg: "))

if food_type == 1:
	print(veg_menu)
elif food_type == 2:
	print(nonveg_menu)
else:
	print("Invalid Entry")

dish_type = input("Enter item code to book your order: ")

print(f"Congratulations, Your order {dish_type} is booked and arriving soon to your door.")

