color = 0
type = 0
amount = 0

print ("""Welcome to Abby’s Merchandizing!
What colour of shirt would you like to order?
1. White 2. Black 3. Red 4. Blue 5. Green 6. Yellow""")

color = str(input("Please pick the number adjacent to the preferred color: "))

if color ==  "1":
    color = "White"
    print ("Thank you. The chosen color is " + color)

elif color ==  "2":
    color = "Black"
    print ("Thank you. The chosen color is " + color)

elif color ==  "3":
    color = "Red"
    print ("Thank you. The chosen color is " + color)

elif color == "4":
    color = "Blue"
    print ("Thank you. The chosen color is " + color)   

elif color ==  "5":
    color = "Green"
    print ("Thank you. The chosen color is " + color)

elif color ==  "6":
    color = "Yellow"
    print ("Thank you. The chosen color is " + color)

else:
    print ("Incorrect value was entered")
    exit ()

print ("What type of shirt would you like to buy?")
type = str(input("Type 1 for Polo. Type 2 for T-shirt: "))

if type ==  "1":
    type = "Polo"
    print ("Thank you. The chosen shirt type is " + type)

elif type ==  "2":
     type = "T-shirt"
     print ("Thank you. The chosen shirt type is " + type)

else:
    print ("Incorrect value was entered")
    exit ()

amount = int(input("How many shirts would you like to purchase: "))
