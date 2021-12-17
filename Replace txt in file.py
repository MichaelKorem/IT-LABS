import re

def replacetext(search_text,replace_text):
    with open('D:\Folder1\SampleFile.txt','r+') as f:

        file = f.read()
        file = re.sub(search_text, replace_text, file)

        f.write(file)

    return "Text replaced"

search_text = "Baljeet"
replace_text = "***Baljeet***"

replacetext(search_text,replace_text)
#Not neccessary from here on----------------------------------
file1 = open('D:\Folder1\SampleFile.txt', "r")
print(file1.read())