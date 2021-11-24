price = 0
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
                type = int(input("Type 1 for Polo. Type 2 for T-shirt: "))
                if type == 1:
                    type = str("Polo")
                    print ("Thank you. The chosen shirt type is " + type)
                    break
                elif type == 2:
                    type = str("T-shirt")
                    print ("Thank you. The chosen shirt type is " + type)
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
                color = int(input("Please pick the number adjacent to the preferred color: "))
                if color ==  1:
                    color = "White"
                    print ("Thank you. The chosen color is " + color)
                    break

                elif color ==  2:
                    color = "Black"
                    print ("Thank you. The chosen color is " + color)
                    break

                elif color ==  3:
                    color = "Red"
                    print ("Thank you. The chosen color is " + color)
                    break

                elif color == 4:
                    color = "Blue"
                    print ("Thank you. The chosen color is " + color)   
                    break

                elif color ==  5:
                    color = "Green"
                    print ("Thank you. The chosen color is " + color)
                    break

                elif color ==  6:
                    color = "Yellow"
                    print ("Thank you. The chosen color is " + color)
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
                amount = int(input("How many shirts would you like to order: "))
                break
            except ValueError:
                print ("Incorrect value was entered. Please try again.")
                continue
            
        float(price) = format((amount * 9.99), ".2f")

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
                type = int(input("Type 1 for Jeans. Type 2 for Chino: "))

                if type ==  1:
                    type = "Jeans"
                    print ("Thank you. The chosen trouser type is " + type)
                    break

                elif type ==  2:
                    type = "Chino"
                    print ("Thank you. The chosen trouser type is " + type)
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
                color = int(input("Please pick the number adjacent to the preferred color: "))

                if color ==  1:
                    color = "Blue"
                    print ("Thank you. The chosen color is " + color)
                    break

                elif color ==  2:
                    color = "Black"
                    print ("Thank you. The chosen color is " + color)
                    break

                elif color ==  3:
                    color = "Grey"
                    print ("Thank you. The chosen color is " + color)
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
                amount = int(input("How many trousers would you like to order: "))
                break
            except ValueError:
                print ("Incorrect value was entered. Please try again.")
                continue

        float(price) = format((amount*14.99), ".2f")

class Calculate:
    def __init__(self, distypeshirt, shirtdis, distypepants, pantdis):
        self.distypeshirt = distypeshirt
        self.shirtdis = shirtdis
        self.distypepants = distypepants
        self.pantdis = pantdis
    
    def calcDiscount():
        distype = 0
        Calculate.shirtdis = 0
        Calculate.pantdis = 0
        counter = ["Y", "y", "N", "n"]
        while distype == 0:
            sytype = input("Are you a senior citizen? Y/N ")

            if distype in counter:
                break

            else:
                print("Incorrect value was entered. Please try again.")
                distype = 0
                continue

        if distype == "y" or distype == "Y":
            Calculate.shirtdis = 0.1
            Calculate.pantdis = 0.1
            Calculate.distypepants = "Senior citizen"
            Calculate.distypeshirt = "Senior citizen"

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
            Calculate.shirtdis = 0.1
            Calculate.pantdis = 0.1
            Calculate.distypepants = "Student"
            Calculate.distypeshirt = "Student"

        if Shirts.amount >= 3:
            Calculate.shirtdis = 0.15
            Calculate.distypeshirt = "Quantity"

        if Pants.amount >= 3:
            Calculate.pantdis = 0.15
            Calculate.distypepants = "Quantity"

    def calcTotal():
        sum = 0
        sum1 = 0
        sum2 = 0
        print ("""
Summary:
_____________________________________________________________

You have ordered """ + str(Shirts.amount) + " " + Shirts.color + " " + Shirts.type + " shirts and " + str(Pants.amount) + " " + Pants.color + " " + Pants.type + " trousers.")
        total = float(Shirts.price) + float(Pants.price)
        total = format(total, ".2f")
        print ("Amount to pay before tax is: " + str(total) + "$")
        
        if Calculate.distypeshirt == Calculate.distypepants:
            sum = Calculate.shirtdis * float(Shirts.price)
            sum += Calculate.pantdis * float(Pants.price)
            sum = format(sum, ".2f")
            print (Calculate.distypeshirt + "discount is: -" + str(sum) + "$")

        else:
            if Calculate.shirtdis > 0:
                sum1 = Calculate.shirtdis * float(Shirts.price)
                sum1 = format(sum1, ".2f")
                print (Calculate.distypeshirt + "discount is: -" + str(sum1) + "$")
        
            if Calculate.pantdis > 0:
                sum2 = Calculate.pantdis * float(Pants.price)
                sum2 = format(sum2, ".2f")
                print (Calculate.distypepants + "discount is: -" + str(sum2) + "$")
        
        price = float(Shirts.price + Pants.price - sum - sum1 - sum2)
        hst = float(price)*0.13
        total = price+hst
        hst = format(hst, ".2f")
        total = format(total, ".2f")
        print("HST is: " + str(hst) + "$")
        print ("Amount to pay including HST is: " + str(total) + "$")

Shirts()
Pants()
Calculate()