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




