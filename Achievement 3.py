x = 0
y = 0
sum = 0

while x <= 0:
    x = int(input("Please enter a positive number: "))
    if x <= 0:
        print ("Wrong number entered. Please try again.")

while y <= x:
    sum += y ** 2
    y += 2

print (sum)