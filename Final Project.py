vocabulary = ["ABSURD", "AWKWARD", "BANDWAGON", "BOOKWORM", "ESPIONAGE", "FUNNY", "GALAXY", "GAZEBO", "GOSSIP", "INJURY", "JAZZ", "JIGSAW", "JUKEBOX", "KEYHOLE", "LENGTH", "LUCKY", "LUXURY", "MATRIX", "OXYGEN", "PIXEL", "PUZZLING", "QUIZ", "RHUBARB", "STRENGTH", "STRONGHOLD", "TRANSCRIPT", "UNKNOWN", "WIZARD", "WRISTWATCH", "ZIPPER"]
counter = 1
wordpresent = ["*"]

m1 = ("""





^^^^^^^^""")
m2 = ("""
|
|
|
|
|
^^^^^^^^""")
m3 = ("""_______
|
|
|
|
|
^^^^^^^^""")
m4 = ("""_______
|     |
|     o
|
|
|
^^^^^^^^""")
m5 = ("""_______
|     |
|     o
|     |
|
|
^^^^^^^^""")
m6 = ("""_______
|     |
|     o
|    /|\ 
|
|
^^^^^^^^""")
m7 = ("""_______
|     |
|     o
|    /|\ 
|    / \ 
|
^^^^^^^^""")

import random
x = random.randint(0, 30)

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