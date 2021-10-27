class Math:
    def __init__(self):
        self.num = []

    def CalcAddition(self):
        print(x+y)

    def CalcSubstraction(self):
        print(x-y)

    def CalcMultiplication(self):
        print(x*y)

    def CalcDivision(self):
        div = x/y
        div = format(div, ".2f")
        print(div)

    def CalcModDivision(self):
        print(x%y)

print("""What type of mathematical operation would you like to perform?
Press 1 for Addition 
Press 2 for Subtraction 
Press 3 for Multiplication 
Press 4 for Division 
Press 5 for Modulus Division""")

while True:
    try:
        op = int(input("Your choice is: "))
        if op == 1:
            op = str("Addition")
            break
        elif op == 2:
            op = str("Substraction")
            break
        elif op == 3:
            op = str("Multiplication")
            break
        elif op == 4:
            op = str("Division")
            break
        elif op == 5:
            op = str("Modulus Division")
            break
        else:
            print ("Incorrect value was entered. Please try again.")
            continue

    except ValueError:
        print ("Incorrect value was entered. Please try again.")
        continue

print ("Thank you. The chosen operation is " + op)

while True:
    try: 
        x = int(input("Please pick the first number: "))
        y = int(input("Please pick the second number: "))

    except ValueError:
        print ("Incorrect value was entered. Please try again.")
        continue

    if op == "Addition":
        Math.CalcAddition(op)
    elif op == "Substraction":
        Math.CalcSubstraction(op)
    elif op == "Multiplication":
        Math.CalcMultiplication(op)
    elif op == "Division":
        Math.CalcDivision(op)
    elif op == "Modulus Division":
        Math.CalcModDivision(op)
    exit()