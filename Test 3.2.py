class Rectangle

def __init__(self):
    self.perimeter = 0
    self.area = 0

def getPerimeter(self):
    length = float(input("Please insert the length of the rectangle:"))
    while True:
            try:
                length = float(format((length), ".2f"))
                break
            except ValueError:
                print("Incorrect value was entered. Please try again.")
                continue
    
    width = float(input("Please insert the width of the rectangle:"))
    while True:
        try:
            width = float(format((width), ".2f"))
            break
        except ValueError:
            print("Incorrect value was entered. Please try again.")
            continue
    
    perimeter = 2*(length+width)
    perimeter = float(format((perimeter), ".2f"))

def 