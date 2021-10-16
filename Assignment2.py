shirtcolour = 0
shirttype = 0
shirtamount = 0
trousercolour = 0
trousertype = 0
trouseramount = 0
sytype = 0
sydiscount = 1
qdiscountshirt = 0
qdiscounttrouser = 0

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

print("""What colour of shirt would you like to order?
1. White 2. Black 3. Red 4. Blue 5. Green 6. Yellow""")
while True:
    try: 
        shirtcolour = int(input("Please pick the number adjacent to the preferred colour: "))
        if shirtcolour ==  1:
            shirtcolour = "White"
            print ("Thank you. The chosen colour is " + shirtcolour)
            break

        elif shirtcolour ==  2:
            shirtcolour = "Black"
            print ("Thank you. The chosen colour is " + shirtcolour)
            break

        elif shirtcolour ==  3:
            shirtcolour = "Red"
            print ("Thank you. The chosen colour is " + shirtcolour)
            break

        elif shirtcolour == 4:
            shirtcolour = "Blue"
            print ("Thank you. The chosen colour is " + shirtcolour)   
            break

        elif shirtcolour ==  5:
            shirtcolour = "Green"
            print ("Thank you. The chosen colour is " + shirtcolour)
            break

        elif shirtcolour ==  6:
            shirtcolour = "Yellow"
            print ("Thank you. The chosen colour is " + shirtcolour)
            break

        else:
            print ("Incorrect value was entered. Please try again.")
            continue

    except ValueError:
        print ("Incorrect value was entered. Please try again.")
        continue

while True:
    try:
        shirtamount = int(input("How many shirts would you like to order: "))
        break
    except ValueError:
        print ("Incorrect value was entered. Please try again.")
        continue

print ("""What type of trousers would you like to order?
1. Jeans - 14.99$ 2. Chino - 14.99$""")
while True:
    try:    
        trousertype = int(input("Type 1 for Jeans. Type 2 for Chino: "))

        if trousertype ==  1:
            trousertype = "Jeans"
            print ("Thank you. The chosen trouser type is " + trousertype)
            break

        elif trousertype ==  2:
            trousertype = "Chino"
            print ("Thank you. The chosen trouser type is " + trousertype)
            break

        else:
            print ("Incorrect value was entered. Please try again.")
            continue

    except ValueError:
        print ("Incorrect value was entered. Please try again.")
        continue

print ("""What colour of trousers would you like to order?
1. Blue 2. Black 3. Grey""")

while True:
    try:   
        trousercolour = int(input("Please pick the number adjacent to the preferred colour: "))

        if trousercolour ==  1:
            trousercolour = "Blue"
            print ("Thank you. The chosen colour is " + trousercolour)
            break

        elif trousercolour ==  2:
            trousercolour = "Black"
            print ("Thank you. The chosen colour is " + trousercolour)
            break

        elif trousercolour ==  3:
            trousercolour = "Grey"
            print ("Thank you. The chosen color is " + trousercolour)
            break

        else:
            print ("Incorrect value was entered. Please try again.")
            continue

    except ValueError:
        print ("Incorrect value was entered. Please try again.")
        continue

while True:
    try:
        trouseramount = int(input("How many trousers would you like to order: "))
        break
    except ValueError:
        print ("Incorrect value was entered. Please try again.")
        continue

counter = ["Y", "y", "N", "n"]
x = 0
while x < len(counter):
    sytype = input("Are you a senior citizen? Y/N ")

    if counter[x] != sytype:
        x += 1
        print ("Incorrect value was entered. Please try again.")
        continue
    else:
        break

if sytype == "y" or sytype == "Y":
    float(sydiscount) = 0.1
    sytype = "Senior citizen"

elif sytype == "n" or sytype == "N":
    x = 0
    
    while x < len(counter):
        sytype = input("Are you a student? Y/N ")

        if counter[x] != sytype:
            x += 1
            print ("Incorrect value was entered. Please try again.")
            continue
        else:
            break

if sytype == "y" or sytype == "Y":
    float(sydiscount) = 0.1
    sytype = "Student"

shirtprice = round((shirtamount*9.99),2)
trouserprice = round((trouseramount*14.99),2)

print ("You have ordered " + str(shirtamount) + " " + shirtcolour + " " + shirttype + " shirts")
print ("and " + str(trouseramount) + " " + trousercolour + " " + trousertype + " trousers.")
print ("total price is : " + str(shirtprice+trouserprice) + "$")

if shirtamount >= 3:
    float(qdiscountshirt) = 0.15

if trouseramount >= 3:
    float(qdiscounttrouser) = 0.15

if qdiscountshirt > 0 or qdiscounttrouser > 0:
    print ("Quantity discount is: ", + (qdiscountshirt*shirtamount)+(qdiscounttrouser*trouseramount))

if sydiscount > qdiscountshirt
print ("Amount to pay including HST is: " + str(shirtprice) + "$")