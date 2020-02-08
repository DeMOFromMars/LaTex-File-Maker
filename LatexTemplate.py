# Latex Template

# By Devin M. O'Brien (MasterOfAllEvil)

def checker(var, options):
    counter = -1
    for x in options:
        counter += 1
        if var == x:
            return counter


def start():
    user = input("Would you like to create a new file or load an existing file (n/l):")
    user = user.upper()
    option = checker(user, ["N", "L"])
    print(str(option))
    if option == 0:
        create()
    else:
        if option == 1:
            load()
        else:
            print("Invalid Input")

def backup(name):
    orig = open(name + ".tex", "r")
    file = open(name + "[BACKUP].tex", "w+")
    data = orig.readlines()
    for x in data:
        file.write(x)
    file.close()


def proc():
    sopUser = input("Would you like sections or paragraphs?(s/p)")
    data = []
    if(sopUser == "p" or sopUser == "P"):
        number = int(input("How many paragraphs?"))
    else:
        number = int(input("How many sections?"))

    num = range(0, number)

    if sopUser == "s" or sopUser == "S":
        for x in num:
            data.append("\\section{Problem " + str(x + 1) + "}\n\n")

    if sopUser == "p" or sopUser == "P":
        for x in num:
            data.append("\\paragraph{Problem " + str(x + 1) + "}\n\n")
    if sopUser == "a" or sopUser == "A":
        for x in range(0, number):
            data.append("\\section{Problem " + str(x + 1) + "}\n\n")
            secondary = 0
            secondary = int(input(str(x + 1) + ").How many subsections?"))
            char = "a"
            i = ord(char[0])

            for x in range(0, secondary):
                char = chr(i)
                data.append("\\subsection{" + char + ".)}\n\n")
                i += 1
    
    return data

def create():
    fileName = input("Please Enter File Name (no extension): ")
    
    file = open(fileName + ".tex", "w+")

    # Creates Header

    file.write("\\documentclass[12pt]{article}\n\n")
    title = input("Title: ")
    file.write("\\title{" + title + "}\n")
    author = input("Author: ")
    file.write("\\author{" + author + "}\n")

    # Creates Body
    file.write("\\begin{document}\n")
    sopUser = input("Would you like sections or paragraphs?(s/p)")

    number = int(input("How many sections?"))

    num = range(0, number)

    if sopUser == "s" or sopUser == "S":
        for x in num:
            file.write("\\section{Problem " + str(x + 1) + "}\n\n")

    if sopUser == "p" or sopUser == "P":
        for x in num:
            file.write("\\paragraph{Problem " + str(x + 1) + "}\n\n")
    if sopUser == "a" or sopUser == "A":
        for x in range(0, number):
            file.write("\\section{Problem " + str(x + 1) + "}\n\n")
            secondary = 0
            secondary = int(input(str(x + 1) + ").How many subsections?"))
            char = "a"
            i = ord(char[0])

            for x in range(0, secondary):
                char = chr(i)
                file.write("\\subsection{" + char + ".)}\n\n")
                i += 1
    file.write("\\end{document}")
    file.close()


def load():
    name = input("File Name: ")
    backup(name)
    file = open(name + ".tex", "r")
    data = file.readlines()
    file.close()
    counter = 0
    location = 0
    for x in data:
        counter += 1
        if x == "<|>\n": #Symbol
            print("Found?" + str(counter))
            print(str(data))
            location = counter
         
    newdata = proc()
    for x in newdata:
        data.insert(location, x)
        location += 1
    
    file = open(name + ".tex", "w")
    for x in data:
        file.write(x)
    file.close()
    print(data[0])



start()

