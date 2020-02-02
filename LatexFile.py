# Attempt to dissect Latex File Anatomy
# Currently Does not doe anything

class Head:
    docClass = "article"  # Currently Only Working With Article Class Type
    mod = "12pt"
    title = "Testing"
    author = "Tester"
    date = "2/1/2020"

    def createDocClass(self):
        return "\\documentclass[" + mod + "]{" + docClass + "}\n"

    def createTitle(self):
        return "\\title{" + title + "}\n"

    def createAuthor(self):
        return "\\author{" + author + "}\n"

    def createDate(self):
        return "\\date{" + date + "}\n"

    def createHead(self):
        createDocClass()
        createTitle()
        createAuthor()
        createDate()


class Body:
    sections
