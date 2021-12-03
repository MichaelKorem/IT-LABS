class Rectangle:

    def __init__(self):
        self.perimeter = 0
        self.area = 0

    def getPerimeter(self,length,width): 
        self.perimeter = 2*(length+width)
        self.perimeter = float(format((self.perimeter), ".2f"))

    def getArea(self,length,width):
        self.area = length*width
        self.area = float(format((self.area), ".2f"))

    def showResults(self):
        print("The rectangle perimeter is:", self.perimeter)
        print("The rectangle area is:", self.area)

length = 0
width = 0
while True:
        try:
            length = float(input("Please insert the length of the rectangle:"))
            length = float(format((length), ".2f"))
            break
        except ValueError:
            print("Incorrect value was entered. Please try again.")
            continue
    
while True:
        try:
            width = float(input("Please insert the width of the rectangle:"))
            width = float(format((width), ".2f"))
            break
        except ValueError:
            print("Incorrect value was entered. Please try again.")
            continue

rectangle = Rectangle()
rectangle.getPerimeter(length,width)
rectangle.getArea(length,width)
rectangle.showResults()