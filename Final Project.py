import random

WordList = ["ABSURD", "AWKWARD", "BANDWAGON", "BOOKWORM", "ESPIONAGE", "FUNNY", "GALAXY", "GAZEBO", "GOSSIP", "INJURY", "JAZZ", "JIGSAW", "JUKEBOX", "KEYHOLE", "LENGTH", "LUCKY", "LUXURY", "MATRIX", "OXYGEN", "PIXEL", "PUZZLING", "QUIZ", "RHUBARB", "STRENGTH", "STRONGHOLD", "TRANSCRIPT", "UNKNOWN", "WIZARD", "WRISTWATCH", "ZIPPER"]

Gallow = ["""  
 +---+     
     |      
     |      
     | 
   =====""",
"""
 +---+     
 O   |      
     |      
     | 
   =====""",
"""
 +---+     
 O   |      
 |   |      
     | 
   =====""",
"""
 +---+     
 O   |      
/|   |      
     | 
   =====""",
"""
 +---+     
 O   |      
/|\  |      
     | 
   =====""",
"""
 +---+     
 O   |      
/|\  |      
/    | 
   =====""",
"""
 +---+     
 O   |      
/|\  |      
/ \  | 
   ====="""]

def RandomWord(WordList):
   WordNum = random.randint(0, len(WordList)-1)
   return WordList[WordNum]

def Interface(WrongGuess, CorrectGuess, ChosenWord):
    if len(WrongGuess) > 0:
        print(Gallow[len(WrongGuess)-1])
        print("""
Wrong guesses:""")
        for Letter in WrongGuess:
            print(Letter, end=" ")
    if len(WrongGuess) >= 0 and len(WrongGuess) < len(ChosenWord):       
        print("""

The secret word is:
""")

        HiddenWord = "_" * len(ChosenWord)

        for i in range(len(ChosenWord)):
            if ChosenWord[i] in CorrectGuess:
                HiddenWord = HiddenWord[:i] + ChosenWord[i] + HiddenWord[i+1:]

        for Letter in HiddenWord:
            print(Letter, end=" ")
        print()
