class Calculator:
    def factorial(sum,num):
        sum = num
        while num-1 > 0:
            sum = sum*(num-1)
            num = num -1
        print(sum)
        
while True:
    try:            
        n = int(input("Please insert a number: "))
    except ValueError:
        print ("Incorrect value was entered. Please try again.")
        continue
    Calculator.factorial(sum,n)
    break 