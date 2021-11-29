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

def LetsPlay(Guesses):
    while True:
        Guess = input("""
Guess a single letter: """)
        Guess = Guess.upper()
        if len(Guess) != 1:
            print("Please enter a single letter.")
        elif Guess in Guesses:
            print("You have already guessed that letter. Try again.")
        elif Guess not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("Please enter a letter.")
        else:
            return Guess

print("""
 _   _   ___   _   _  _____ ___  ___  ___   _   _ 
| | | | / _ \ | \ | ||  __ \|  \/  | / _ \ | \ | |
| |_| |/ /_\ \|  \| || |  \/| .  . |/ /_\ \|  \| |
|  _  ||  _  || . ` || | __ | |\/| ||  _  || . ` |
| | | || | | || |\  || |_\ \| |  | || | | || |\  |
\_| |_/\_| |_/\_| \_/ \____/\_|  |_/\_| |_/\_| \_/
                                                  
                                                  
Welcome to HANGMAN Game!
Your objective is to guess the secret word.
You can guess only a single letter at a time.
You can make up to 7 mistakes. And then you hang!
Let’s begin!""")
WrongGuess = ""
CorrectGuess = ""
ChosenWord = RandomWord(WordList)
Finished = False

while True:
    Interface(WrongGuess, CorrectGuess, ChosenWord)
 
    Guess = LetsPlay(WrongGuess + CorrectGuess)
 
    if Guess in ChosenWord:
        print("""
You are correct! The letter:""", Guess, "is in the secret word.""")
        CorrectGuess = CorrectGuess + Guess
 
        Victory = True
        for i in range(len(ChosenWord)):
            if ChosenWord[i] not in CorrectGuess:
                Victory = False
                break
        if Victory:
            print("""
Well Done! The secret word is """ + ChosenWord)
            print("""
__  __ ____   __  __   _       __ ____ _   __ __
\ \/ // __ \ / / / /  | |     / //  _// | / // /
 \  // / / // / / /   | | /| / / / / /  |/ // / 
 / // /_/ // /_/ /    | |/ |/ /_/ / / /|  //_/  
/_/ \____/ \____/     |__/|__//___//_/ |_/(_)   
                                                """)
            Finished = True
    else:
        print("""
Wrong guess! The letter: """ + Guess, "is not in the secret word.")
        WrongGuess = WrongGuess + Guess

        if len(WrongGuess) == 7:
            Interface(WrongGuess, CorrectGuess, ChosenWord)
            print(Gallow[len(WrongGuess)-1])
            print("""
You have run out of guesses! The word was """ + ChosenWord)
            print("""
#     # ####### #     #    #       #######  #####  ####### 
 #   #  #     # #     #    #       #     # #     # #       
  # #   #     # #     #    #       #     # #       #       
   #    #     # #     #    #       #     #  #####  #####   
   #    #     # #     #    #       #     #       # #       
   #    #     # #     #    #       #     # #     # #       
   #    #######  #####     ####### #######  #####  #######""")
            Finished = True

    if Finished:
        if PlayAgain():
            WrongGuess = ""
            CorrectGuess = ""
            Finished = False
            ChosenWord = RandomWord(WordList)
        else:
            break