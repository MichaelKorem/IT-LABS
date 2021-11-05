vocabulary = ["ABSURD", "AWKWARD", "BANDWAGON", "BOOKWORM", "ESPIONAGE", "FUNNY", "GALAXY", "GAZEBO", "GOSSIP", "INJURY", "JAZZ", "JIGSAW", "JUKEBOX", "KEYHOLE", "LENGTH", "LUCKY", "LUXURY", "MATRIX", "OXYGEN", "PIXEL", "PUZZLING", "QUIZ", "RHUBARB", "STRENGTH", "STRONGHOLD", "TRANSCRIPT", "UNKNOWN", "WIZARD", "WRISTWATCH", "ZIPPER"]
counter = 1
wordpresent = ["*"]

m1 = ("""  
 +---+     
     |      
     |      
     | 
   =====""")
m2 = ("""
 +---+     
 O   |      
     |      
     | 
   =====""")
m3 = ("""
 +---+     
 O   |      
 |   |      
     | 
   =====""")
m4 = ("""
 +---+     
 O   |      
/|   |      
     | 
   =====""")
m5 = ("""
 +---+     
 O   |      
/|\  |      
     | 
   =====""")
m6 = ("""
 +---+     
 O   |      
/|\  |      
/    | 
   =====""")
m7 = ("""
 +---+     
 O   |      
/|\  |      
/ \  | 
   =====""")

import random
x = random.randint(0, len(vocabulary)-1)

word = vocabulary(x)
wordlist = list(word)

while counter < len(wordlist):
    wordpresent.append("*")



print(m1)
print(m2)
print(m3)
print(m4)
print(m5)
print(m6)
print(m7)