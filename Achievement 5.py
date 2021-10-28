source = "Lorem ipsum doflor szit ametß, consqecytetu$r adipibsching elit, sed do eiusmod tewmporα incid6kgidunt ut labq8ore et café dolore_ magna aliqua. Purus! sit{|}~ \t\n\r\x0b\x0c amet volutpat cons&jequat mau7ris. MichaelKorem8757102Penaxtibus et"

class Characters:
    def CountName(self):
        x = source.count('M')+source.count('m')
        print("Found", str(x), "matches of the letter M")

    def CountNum(self):
        counter = 0
        for n in source:  
            if n.isdigit():      
                counter +=1
            else:    
               pass       
        print("Found", str(counter), "matches of digits")

    def CountAlNum(self):
        counter = 0
        for n in source:  
            if n.isalnum():      
                counter +=1
            else:    
               pass       
        print("Found", str(counter), "matches of alphanumeric characters")


    def CountNonAlNum(self):
        counter = 0
        for n in source:  
            if n.isalnum():      
                counter +=1
            else:    
               pass       
        print("Found", str(len(source)-counter), "matches of non-alphanumeric characters")

    def CountSpace(self):
         print("Found", str(source.count(' ')), "number of spaces")

Characters.CountName(source)
Characters.CountNum(source)
Characters.CountAlNum(source)
Characters.CountNonAlNum(source)
Characters.CountSpace(source)