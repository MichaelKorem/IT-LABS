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
