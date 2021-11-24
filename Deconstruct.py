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
                Shirts.type = int(input("Type 1 for Polo. Type 2 for T-shirt: "))
                if Shirts.type == 1:
                    Shirts.type = str("Polo")
                    print ("Thank you. The chosen shirt type is " + Shirts.type)
                    break
                elif Shirts.type == 2:
                    Shirts.type = str("T-shirt")
                    print ("Thank you. The chosen shirt type is " + Shirts.type)
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
                Shirts.color = int(input("Please pick the number adjacent to the preferred color: "))
                if Shirts.color ==  1:
                    Shirts.color = "White"
                    print ("Thank you. The chosen color is " + Shirts.color)
                    break

                elif Shirts.color ==  2:
                    Shirts.color = "Black"
                    print ("Thank you. The chosen color is " + Shirts.color)
                    break

                elif Shirts.color ==  3:
                    Shirts.color = "Red"
                    print ("Thank you. The chosen color is " + Shirts.color)
                    break

                elif Shirts.color == 4:
                    Shirts.color = "Blue"
                    print ("Thank you. The chosen color is " + Shirts.color)   
                    break

                elif Shirts.color ==  5:
                    Shirts.color = "Green"
                    print ("Thank you. The chosen color is " + Shirts.color)
                    break

                elif Shirts.color ==  6:
                    Shirts.color = "Yellow"
                    print ("Thank you. The chosen color is " + Shirts.color)
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
                Shirts.amount = int(input("How many shirts would you like to order: "))
                break
            except ValueError:
                print ("Incorrect value was entered. Please try again.")
                continue

Shirts(type, color, amount, price)