x = 0
x = str(input("Please enter one capital or low key letter "))
len (x)
1

if x.isupper ():
    print ("Your letter was changed to lower case: " + x.lower ())

elif x.islower ():
    print ("Your letter was changed to upper case: " + x.upper ())

else:
    print ("Incorrect value was entered")