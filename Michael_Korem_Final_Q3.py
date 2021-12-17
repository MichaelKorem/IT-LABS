import datetime

now = datetime.datetime.now()

class AnalyzeTriangle:

    def __init__(self):
        pass

    def validateTriangle():
        
        while True:
                try:
                    angle1 = int(input("Please insert the first angle of the triangle:"))
                    angle2 = int(input("Please insert the second angle of the triangle:"))
                    angle3 = int(input("Please insert the third angle of the triangle:"))
                    break
                except ValueError:
                    print("Incorrect value was entered. Please try again.")
                    continue
    
        if angle1+angle2+angle3 == 180:
            print("The triangle is formed")
            if angle1 == angle2 and angle1 == angle3:
                print("The triangle is Equilateral")
            elif (angle1 == angle2) or (angle1 == angle3) or (angle2 == angle3):
                print("The triangle is Isosceles")
            else:
                print("The triangle is Scalene")
        else:
            print("The triangle is not formed")

        print(now.strftime("%m:%d:%Y %H:%M:%S"))
        
AnalyzeTriangle.validateTriangle()