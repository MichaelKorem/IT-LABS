class Shirts:
    def __init__(self):
        self.type = ""
        self.color = ""
        self.amount = 0
        self.price = 0

    def orderDetails(self):
        print("""
What type of shirt would you like to order?
1. Polo - 9.99$ 2. T-shirt - 9.99$""")

        while True:
            try:
                selection = int(input("Type 1 for Polo. Type 2 for T-shirt: "))
                if selection == 1:
                    self.type = str("Polo")
                    print("Thank you. The chosen shirt type is " + self.type)
                    break
                elif selection == 2:
                    self.type = str("T-shirt")
                    print("Thank you. The chosen shirt type is " + self.type)
                    break
                else:
                    print("Incorrect value was entered. Please try again.")
                    continue

            except ValueError:
                print("Incorrect value was entered. Please try again.")
                continue

        print("""
What color of shirt would you like to order?
1. White 2. Black 3. Red 4. Blue 5. Green 6. Yellow""")
        while True:
            try:
                selection = int(input("Please pick the number adjacent to the preferred color: "))
                if selection == 1:
                    self.color = "White"
                    print("Thank you. The chosen color is " + self.color)
                    break

                elif selection == 2:
                    self.color = "Black"
                    print("Thank you. The chosen color is " + self.color)
                    break

                elif selection == 3:
                    self.color = "Red"
                    print("Thank you. The chosen color is " + self.color)
                    break

                elif selection == 4:
                    self.color = "Blue"
                    print("Thank you. The chosen color is " + self.color)
                    break

                elif selection == 5:
                    self.color = "Green"
                    print("Thank you. The chosen color is " + self.color)
                    break

                elif selection == 6:
                    self.color = "Yellow"
                    print("Thank you. The chosen color is " + self.color)
                    break

                else:
                    print("""Incorrect value was entered. Please try again.
1. White 2. Black 3. Red 4. Blue 5. Green 6. Yellow""")
                    continue

            except ValueError:
                print("""Incorrect value was entered. Please try again.
1. White 2. Black 3. Red 4. Blue 5. Green 6. Yellow""")
                continue

        while True:
            try:
                self.amount = int(input("""
How many shirts would you like to order: """))
                break
            
            except ValueError:
                print("Incorrect value was entered. Please try again.")
                continue

        self.price = float(format((self.amount * 9.99), ".2f"))

class Pants:
    def __init__(self):
        self.type = ""
        self.color = ""
        self.amount = 0
        self.price = 0

    def orderDetails(self):
        print("""
What type of pants would you like to order?
1. Jeans - 14.99$ 2. Chino - 14.99$""")
        while True:
            try:
                selection = int(input("Type 1 for Jeans. Type 2 for Chino: "))

                if selection == 1:
                    self.type = "Jeans"
                    print("Thank you. The chosen pants type is " + self.type)
                    break

                elif selection == 2:
                    self.type = "Chino"
                    print("Thank you. The chosen pants type is " + self.type)
                    break

                else:
                    print("Incorrect value was entered. Please try again.")
                    continue

            except ValueError:
                print("Incorrect value was entered. Please try again.")
                continue

        print("""
What color of pants would you like to order?
1. Blue 2. Black 3. Grey""")

        while True:
            try:
                selection = int(input("Please pick the number adjacent to the preferred color: "))

                if selection == 1:
                    self.color = "Blue"
                    print("Thank you. The chosen color is " + self.color)
                    break

                elif selection == 2:
                    self.color = "Black"
                    print("Thank you. The chosen color is " + self.color)
                    break

                elif selection == 3:
                    self.color = "Grey"
                    print("Thank you. The chosen color is " + self.color)
                    break

                else:
                    print("""Incorrect value was entered. Please try again.
1. Blue 2. Black 3. Grey""")
                    continue

            except ValueError:
                print("""Incorrect value was entered. Please try again.
1. Blue 2. Black 3. Grey""")
                continue

        while True:
            try:
                self.amount = int(input("""
How many pants would you like to order: """))
                break
            
            except ValueError:
                print("Incorrect value was entered. Please try again.")
                continue

        self.price = float(format((self.amount * 14.99), ".2f"))


class Calculate:
    def __init__(self, boughtshirts, boughtpants):
        self.distypeshirt = ""
        self.shirtdis = 0
        self.distypepants = ""
        self.pantdis = 0
        self.boughtshirts = boughtshirts
        self.boughtpants = boughtpants

    def calcDiscount(self):
        self.shirtdis = 0
        self.pantdis = 0
        counter = ["Y", "y", "N", "n"]

        if self.boughtshirts.amount < 3 or self.boughtpants.amount < 3:
            while True:
                distype = input("""
Are you a senior citizen? Y/N """)

                if distype in counter:
                    break

                else:
                    print("Incorrect value was entered. Please try again.")
                    continue

            if distype == "y" or distype == "Y":
                self.shirtdis = 0.1
                self.pantdis = 0.1
                self.distypepants = "Senior citizen"
                self.distypeshirt = "Senior citizen"

            while distype == "n" or distype == "N":
                distype = input("Are you a student? Y/N ")
                
                if distype == "y" or distype == "Y":
                    self.shirtdis = 0.1
                    self.pantdis = 0.1
                    self.distypepants = "Student"
                    self.distypeshirt = "Student"
                
                if distype in counter:
                    break
                else:
                    print("Incorrect value was entered. Please try again.")
                    continue

        if self.boughtshirts.amount >= 3:
            self.shirtdis = 0.15
            self.distypeshirt = "Quantity"

        if self.boughtpants.amount >= 3:
            self.pantdis = 0.15
            self.distypepants = "Quantity"

    def calcTotal(self):
        summary = 0
        sum1 = 0
        sum2 = 0
        print("""
Summary:
_____________________________________________________________

You have ordered """ + str(self.boughtshirts.amount) + " " + self.boughtshirts.color + " "
              + self.boughtshirts.type + " shirts and " + str(self.boughtpants.amount) + " "
              + self.boughtpants.color + " " + self.boughtpants.type + " trousers.")
        total = float(self.boughtshirts.price) + float(self.boughtpants.price)
        total = format(total, ".2f")
        print("Amount to pay before tax is: " + str(total) + "$")

        if self.distypeshirt == self.distypepants:
            summary = self.shirtdis * float(self.boughtshirts.price)
            summary += self.pantdis * float(self.boughtpants.price)
            valsummary = format(summary, ".2f")
            print(str(self.distypeshirt) + " discount is: -" + str(valsummary) + "$")

        else:
            if self.shirtdis > 0:
                sum1 = self.shirtdis * float(self.boughtshirts.price)
                valsum1 = format(sum1, ".2f")
                print(self.distypeshirt + " discount is: -" + str(valsum1) + "$")

            if self.pantdis > 0:
                sum2 = self.pantdis * float(self.boughtpants.price)
                valsum2 = format(sum2, ".2f")
                print(self.distypepants + " discount is: -" + str(valsum2) + "$")

        price = float(self.boughtshirts.price + self.boughtpants.price - summary - sum1 - sum2)
        hst = float(price) * 0.13
        total = price + hst
        hst = format(hst, ".2f")
        total = format(total, ".2f")
        print("HST is: " + str(hst) + "$")
        print("Amount to pay including HST is: " + str(total) + "$")


class Shop:

    def Shopping(self):
        print("""+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|W|e|l|c|o|m|e| |t|o| |A|b|b|y|s| |M|e|r|c|h|a|n|d|i|z|i|n|g|!|
+-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+""")

        shirts = Shirts()
        pants = Pants()

        shirts.orderDetails()
        pants.orderDetails()

        calculate = Calculate(shirts, pants)
        calculate.calcDiscount()
        calculate.calcTotal()

shop = Shop()
shop.Shopping()
