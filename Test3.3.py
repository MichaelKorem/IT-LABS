n = int(input("Enter the ending number: "))
sum = 0

for num in range(1, n + 1):
    sum = sum + num
print("The sum of the first", n, "numbers is: ", sum)
average = sum / (n)
print("The average of the first", n, "numbers is: ", average)