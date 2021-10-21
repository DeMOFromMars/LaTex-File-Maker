# Latex File Maker
# Version 1.2
# Modified 10/21/21
# By Devin (MasterOfAllEvil)
# Creates a LaTeX file using an interactive prompt


from src import Command, DocumentClass, Section

def start():
    """Presents LaTeX File Maker's main menu"""
    print("LaTex File Maker\n===============")

    # Menu Options
    options = [
        ("N", "Create a new LaTeX file", create),
        ("L", "Edit an existing LaTeX file", load),
        ("Q", "Quit Program", quit)
    ]
    print("Options\n===========\n")
    for option in options:
        print(option[0] + "   " + option[1] + "\n")

    # User Selection
    user = input()
    user = user.upper()
    valid = False
    for option in options:
        if option[0] == user:
            valid = True
            option[2]()
    if not valid:
        print("Invalid Command")

def quit():
    print("Exiting")

def backup(name):
    """Simple backup to prevent data loss"""
    original = open(name + ".tex", "r")
    file = open(name + "[BACKUP].tex", "w+")
    content = original.readlines()
    for line in content:
        file.write(line)
    file.close()

def proc():
    """Returns an array of sections from user input."""
    sopUser = input("Would you like sections or paragraphs?(s/p/a)")
    data = []
    if(sopUser == "p" or sopUser == "P"):
        number = int(input("How many paragraphs?"))
    else:
        number = int(input("How many sections?"))

    num = range(0, number)
    # Sections
    if sopUser == "s" or sopUser == "S":
        for x in num:
            data.append(
                Section.Section("Problem " + str(x+1), Section.Level.SECTION))
    # Paragraphs
    if sopUser == "p" or sopUser == "P":
        for x in num:
            data.append(
                Section.Section("Problem" + str(x+1), Section.Level.PARAGRAPH)
            )
    # Custom
    if sopUser == "a" or sopUser == "A":
        for x in range(0, number):
            data.append(
                Section.Section("Problem " +str(x+1), Section.Level.SUBSECTION)
            )
            secondary = 0
            secondary = int(input(str(x + 1) + ").How many subsections?"))
            char = "a"
            i = ord(char[0])

            for x in range(0, secondary):
                char = chr(i)
                data.append(
                    Section.Section(char +".", Section.Level.SUBSECTION)
                )
                i += 1
    return data

def create():
    fileName = input("Please Enter File Name (no extension): ")
    doc = []


    # Creates Header

    doc.append(DocumentClass.DocumentClass("article", ["12pt"]))
    title = input("Title: ")
    doc.append(Command.Command("title", None, [title]))
    author = input("Author: ")
    doc.append(Command.Command("author", None, [author]))


    # Creates Body
    doc.append(Command.Command("begin",[],["document"]))
    sopUser = input("Would you like sections or paragraphs?(s/p)")

    number = int(input("How many sections?"))

    num = range(0, number)

    if sopUser == "s" or sopUser == "S":
        for x in num:
            doc.append(Section.Section(""))

    if sopUser == "p" or sopUser == "P":
        for x in num:
            doc.append(Section.Section("",Section.Level.PARAGRAPH))

    if sopUser == "a" or sopUser == "A":
        for x in range(0, number):
            doc.append(Section.Section("Problem " + str(x+1)))
            secondary = int(input(str(x + 1) + ").How many subsections?"))
            char = "a"
            i = ord(char[0])
            for x in range(0, secondary):
                char = chr(i)
                doc.append(Section.Section(char + ".)"))
                i += 1

    doc.append(Command.Command("end", [], ["document"]))
    file = open(fileName + ".tex", "w+")
    for line in doc:
        if line != '\n':
            file.write(str(line) + "\n")
    file.close()


def load():
    """Load document from file"""
    name = input("Please Enter File Name (no extension): ")
    backup(name)
    file = open(name + ".tex", "r")
    content = file.readlines()
    file.close()
    edit(content)
    file = open(name + ".tex", "w")
    for x in content:
        if type(x) is not str:
            file.write(str(x) + "\n")
        else:
            file.write(x)
    file.close()
    print(content[0])
    
def edit(data):
    """Edit document data"""
    ex = False
    while ex is False:
        count = 1 # Option Count
        for x in data:
            temp = str(x)
            if(x is None or len(temp) > 20):
                temp = temp[0:19]
            print(str(count) + "). " + temp)
            count = count + 1
        user = int(input())
        if(user == 0):
            return data
        if(user < 1 or user > len(data)):
            print("Invalid Input")
        else:
            print("What Operation? (aDD/dELETE)")
            user2 = input()
            if user2 == "a":
                title = Section.Section(input())
                data.insert(user - 1, title)
            else:
                if(user2 ==  "d"):
                    data.pop(user - 1)
                else:
                    print("Bad Value")
            
            
    


def __main__():
    start()
    
if __name__ == "__main__":
    __main__()

