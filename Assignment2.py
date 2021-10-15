shirtcolour = 0
shirttype = 0
shirtamount = 0
trousercolour = 0
trousertype = 0
trouseramount = 0

print ("Welcome to Abby’s Merchandizing!")
print("""What type of shirt would you like to order?
1. Polo - 9.99$ 2. T-shirt - 9.99$""")

while True:
    try:
        shirttype = int(input("Type 1 for Polo. Type 2 for T-shirt: "))
        if shirttype == 1:
            shirttype = str("Polo")
            print ("Thank you. The chosen shirt type is " + shirttype)
            break
        elif shirttype == 2:
            shirttype = str("T-shirt")
            print ("Thank you. The chosen shirt type is " + shirttype)
            break
        else:
            print ("Incorrect value was entered. Please try again.")
            continue

    except ValueError:
        print ("Incorrect value was entered. Please try again.")
        continue


while shirtcolour > 1 or shirtcolour <= 6:
    try:
        print("""What colour of shirt would you like to order?
        1. White 2. Black 3. Red 4. Blue 5. Green 6. Yellow""")
        shirtcolour = str(input("Please pick the number adjacent to the preferred colour: "))
    except ValueError:
        print ("Incorrect value was entered. Please try again.")

        if shirtcolour ==  "1":
            shirtcolour = "White"
            print ("Thank you. The chosen colour is " + shirtcolour)
            break

        elif shirtcolour ==  "2":
            shirtcolour = "Black"
            print ("Thank you. The chosen colour is " + shirtcolour)
            break

        elif shirtcolour ==  "3":
            shirtcolour = "Red"
            print ("Thank you. The chosen colour is " + shirtcolour)
            break

        elif shirtcolour == "4":
            shirtcolour = "Blue"
            print ("Thank you. The chosen colour is " + shirtcolour)   
            break

        elif shirtcolour ==  "5":
            shirtcolour = "Green"
            print ("Thank you. The chosen colour is " + shirtcolour)
            break

        elif shirtcolour ==  "6":
            shirtcolour = "Yellow"
            print ("Thank you. The chosen colour is " + shirtcolour)
            break

shirtamount = int(input("How many shirts would you like to order: "))
shirtprice = round((shirtamount*9.99*1.13),2)

while trousertype <= 0:
    print ("""What type of trousers would you like to order?
    1. Jeans - 14.99$ 2. Chino - 14.99$""")
    trousertype = str(input("Type 1 for Jeans. Type 2 for Chino: "))

    if trousertype ==  "1":
        trousertype = "Jeans"
        print ("Thank you. The chosen trouser type is " + trousertype)

    elif trousertype ==  "2":
        trousertype = "Chino"
        print ("Thank you. The chosen trouser type is " + trousertype)

    else:
        print ("Incorrect value was entered. Please try again.")

while trousercolour <= 0:
    print ("""What colour of trousers would you like to order?
    1. Blue 2. Black 3. Grey""")
    trousercolour = str(input("Please pick the number adjacent to the preferred colour: "))

    if trousercolour ==  "1":
        trousercolour = "Blue"
        print ("Thank you. The chosen colour is " + trousercolour)

    elif trousercolour ==  "2":
        trousercolour = "Black"
        print ("Thank you. The chosen colour is " + trousercolour)

    elif trousercolour ==  "3":
        trousercolour = "Grey"
        print ("Thank you. The chosen color is " + trousercolour)

    else:
        print ("Incorrect value was entered. Please try again.")

trouseramount = int(input("How many trousers would you like to order: "))
trouserprice = round((trouseramount*14.99*1.13),2)

print ("You have ordered " + str(shirtamount) + " " + shirtcolor + " " + shirttype + " shirts.")
print ("Amount to pay including HST is: " + str(shirtprice) + "$")