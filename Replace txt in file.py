import re

def replacetext(search_text,replace_text):
    with open('C:\PROG1783 Final Exam\PROG1783File2.txt','r+') as f:

        file = f.read()
        file1 = re.sub(search_text, replace_text, file)
    with open('C:\PROG1783 Final Exam\PROG1783File2.txt','w+') as f:
        f.write(file1)

    return "Text replaced"

search_text = "Michael"
replace_text = "********"

replacetext(search_text,replace_text)
file = open('C:\PROG1783 Final Exam\PROG1783File2.txt', "r")
print(file.read())