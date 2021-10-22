count = 0

text = str(input("Please insert a word: "))

x = list(text)

print(str(x))

while count < len(x):
    if x[count].lower == x[count]:
        x[count] = x[count].upper()
        count = count+1
        continue
        
    if x[count].isupper:
        x[count] = x[count].lower()
        count = count+1
        continue

print("".join(x))