class Temperature:
    def __init__(self, name):
        self.name = name
        self.temp = []

    def insertTemp(self):
        for i in range(3):
            m = int(input("Enter the temperature in %s on day %d :"%(self.name,i+1)))
            self.temp.append(m)
    
    def PrintTemp(self):
        print(self.name, " recorded the following temperatures ", self.temp)

    def CalcAverage(self):
        x = sum(self.temp)
        average = x/len(self.temp)
        print("The average temperature for %s across these days was: " %str(self.name),str(average))