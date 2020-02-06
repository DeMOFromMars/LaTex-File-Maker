# Attempt to dissect Latex File Anatomy
# Currently Does not doe anything
class LatexFile
    class Head:

        def createDocClass(self):
            return '\\documentclass[' + mod + ']{' + docClass + '}\n'

        def createTitle(self):
            return '\\title{' + self.title + '}\n'

        def createAuthor(self):
            return '\\author{' + str(self.author) + '}'

        def createDate(self):
            return '\\date{' + date + '}\n'

        def getAuthor(self):
            return str(self.author)

        def

        def __init__(self, doctype = "article", mod = "12pt", title = "Test", author = "tester", date = "2/2/2020"):
            self.doctype = doctype
            self.title = title
            self.author = author
            self.mod = mod
            self.date = date

        def __str__(self):
            return "Title: " + self.title + "; Author: " + self.author + "; Date: " + self.date + "; DocType: " + self.doctype + "; Modifiers: " + self.mod
    class Body:
        

current = Head()
print(str(current))
