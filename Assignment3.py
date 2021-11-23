shirtprice = 0
trouserprice = 0
x = 0
y = 0
total = 0

class Shirts:
    def __init__(self, type, color, amount, price):
        self.type = type
        self.color = color
        self.amount = amount
        self.price = price
    
    def BuyShirts():
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

        print("""What color of shirt would you like to order?
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
                    print ("""Incorrect value was entered. Please try again.
1. White 2. Black 3. Red 4. Blue 5. Green 6. Yellow""")
                    continue

            except ValueError:
                print ("""Incorrect value was entered. Please try again.
1. White 2. Black 3. Red 4. Blue 5. Green 6. Yellow""")
                continue

        while True:
            try:
                shirtamount = int(input("How many shirts would you like to order: "))
                break
            except ValueError:
                print ("Incorrect value was entered. Please try again.")
                continue
            
        float(shirtprice) = format((shirtamount*9.99), ".2f")

class Pants:
    def __init__(self, type, color, amount, price):
        self.type = type
        self.color = color
        self.amount = amount
        self.price = price
    
    def BuyPants():
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

        print ("""What color of trousers would you like to order?
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
                    print ("""Incorrect value was entered. Please try again.
1. Blue 2. Black 3. Grey""")
                    continue

            except ValueError:
                print ("""Incorrect value was entered. Please try again.
1. Blue 2. Black 3. Grey""")
                continue

        while True:
            try:
                trouseramount = int(input("How many trousers would you like to order: "))
                break
            except ValueError:
                print ("Incorrect value was entered. Please try again.")
                continue

        float(trouserprice) = format((trouseramount*14.99), ".2f")

class Calculate:
    def __init__(self, type, discount):
        self.type = type
        self.discount = discount
    
    def calcDiscount(self):
        sytype = 0
        counter = ["Y", "y", "N", "n"]
        while sytype == 0:
            sytype = input("Are you a senior citizen? Y/N ")

            if sytype in counter:
                break

            else:
                print("Incorrect value was entered. Please try again.")
                sytype = 0
                continue

        if sytype == "y" or sytype == "Y":
            sydiscountshirt = 0.1
            sydiscounttrouser = 0.1
            sytype = "Senior citizen"

        else:
            sytype = 0
    
            while sytype == 0:
                sytype = input("Are you a student? Y/N ")

                if sytype in counter:
                    break
                else:
                    print("Incorrect value was entered. Please try again.")
                    sytype = 0
                    continue

        if sytype == "y" or sytype == "Y":
            sydiscountshirt = 0.1
            sydiscounttrouser = 0.1
            sytype = "Student"

    def calcTotal():
        print ("""
Summary:
_____________________________________________________________

You have ordered """ + str(Shirts.amount) + " " + Shirts.color + " " + Shirts.type + " shirts and " + str(Pants.amount) + " " + Pants.color + " " + Pants.type + " trousers.")
        total = float(Shirts.price) + float(Pants.price)
        total = format(total, ".2f")
        print ("Amount to pay before tax is: " + str(total) + "$")

        if Shirts.amount >= 3:
            qdiscountshirt = 0.15
            sydiscountshirt = 0

        if Pants.amount >= 3:
            qdiscounttrouser = 0.15
            sydiscounttrouser = 0

        if qdiscountshirt > 0 or qdiscounttrouser > 0:
            sum = qdiscountshirt * float(Shirts.price)
            sum += qdiscounttrouser * float(Pants.price)
            sum = format(sum, ".2f")
            print ("Quantity discount is: -" + str(sum) + "$")

        if sydiscountshirt > qdiscountshirt:
            x = format((float(Shirts.price)*sydiscountshirt), ".2f")
        if sydiscounttrouser > qdiscounttrouser:
            y = format((float(Pants.price)*sydiscounttrouser), ".2f")

        if sydiscountshirt > 0 or sydiscounttrouser > 0:
            sum = float(x)+float(y)
            print (Calculate.type + " discount is: -" + str(sum) + "$")

        price = float(Shirts.price)*(1-qdiscountshirt-sydiscountshirt)+float(Pants.price)*(1-qdiscounttrouser-sydiscounttrouser)
        hst = float(price)*0.13
        sum = price+hst
        price = format(price, ".2f")
        hst = format(hst, ".2f")
        sum = format(sum, ".2f")
        print("HST is: " + str(hst) + "$")
        print ("Amount to pay including HST is: " + str(sum) + "$")
