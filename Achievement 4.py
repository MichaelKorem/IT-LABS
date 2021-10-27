class Math:
    def __init__(self, name):
        self.name = name
        self.num = []
    
    def Operation(self):
        print("""What type of mathematical operation would you like to perform?
Press 1 for Addition 
Press 2 for Subtraction 
Press 3 for Multiplication 
Press 4 for Division 
Press 5 for Modulus Division.""")

        while True:
            try:
                self.name = int(input("Your choice is: "))
                if self.name == 1:
                    self.name = str("Addition")
                    break
                elif self.name == 2:
                    self.name = str("Substraction")
                    break
                elif self.name == 3:
                    self.name = str("Multiplication")
                    break
                elif self.name == 4:
                    self.name = str("Division")
                    break
                elif self.name == 5:
                    self.name = str("Modulus Division")
                    break
                else:
                    print ("Incorrect value was entered. Please try again.")
                    continue

            except ValueError:
                print ("Incorrect value was entered. Please try again.")
                continue

        print ("Thank you. The chosen operation is" + self.name)

        while True:
            try: 
                x = int(input("Please pick the first number: "))
                y = int(input("Please pick the second number: "))
                self.num.append(int(x))
                self.num.append(int(y))
            
            except ValueError:
                print ("Incorrect value was entered. Please try again.")
                continue

    def CalcAddition(self):
        print(sum(self.num))

    def CalcSubstraction(self):
        sub = self.num(0)-self.num(1)
        print(sub)

    def CalcMultiplication(self):
        mult = self.num(0)*self.num(1)
        print(mult)

    def CalcDivision(self):
        div = self.num(0)/self.num(1)
        div = format(div, ".2f")
        print(div)

    def CalcModDivision(self):
        mod = self.num(0)%self.num(1)
        mod = format(mod, ".2f")
        print(mod)




      