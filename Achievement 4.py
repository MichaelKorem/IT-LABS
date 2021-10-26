print("""What type of mathematical operation would you like to perform?
Press 1 for Addition 
Press 2 for Subtraction 
Press 3 for Multiplication 
Press 4 for Division 
Press 5 for Modulus Division.""")

while True:
    try:
        op = int(input("Your choice is: "))
        if op == 1:
            print ("Thank you. The chosen shirt type is Addition")
            break
        elif op == 2:
            print ("Thank you. The chosen shirt type is Substraction")
            break
        elif op == 3:
            print ("Thank you. The chosen shirt type is Multiplication")
            break
        elif op == 4:
            print ("Thank you. The chosen shirt type is Division")
            break
        elif op == 5:
            print ("Thank you. The chosen shirt type is Modulus Division")
            break
        else:
            print ("Incorrect value was entered. Please try again.")
            continue

    except ValueError:
        print ("Incorrect value was entered. Please try again.")
        continue

        