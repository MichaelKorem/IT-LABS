x = 0
len (x)
1
x = str(input("Please enter a capital or low key letter "))

if x.isupper ():
    print (x.lower)

elif x.islower ():
    print (x.upper)

else:
    print ("Incorrect value was entered")