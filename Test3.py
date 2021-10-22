class Temperature:
    def __init__(self, name):
        self.name = name
        self.temp = []

    def EnterTemp(self):
        for n in range(3):
            m = float(input("Enter the temperature in %s on day %d :"%(self.name,n+1)))
            m = format((m), ".1f")
            self.temp.append(float(m))
    
    def DisplayTemp(self):
        print(self.name, "recorded the following temperatures", self.temp)

    def CalcAverageTemp(self):
        x = sum(self.temp)
        average = x/len(self.temp)
        average = format((average), ".1f")
        print("The average temperature for %s across these days was:" %str(self.name),str(average))

measure1 = Temperature("Toronto")
measure1.EnterTemp()

measure2 = Temperature("Vancouver")
measure2.EnterTemp()

measure3 = Temperature("Montreal")
measure3.EnterTemp()

measure1.DisplayTemp()
measure2.DisplayTemp()
measure3.DisplayTemp()

measure1.CalcAverageTemp()
measure2.CalcAverageTemp()
measure3.CalcAverageTemp()