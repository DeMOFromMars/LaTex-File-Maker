# Latex Template
# By Devin M. O'Brien (MasterOfAllEvil)



fileName = input("Please Enter File Name (no extension): ")
file = open(fileName + ".tex", "w+")
file.write("\\documentclass[12pt]{article}\n\n")

title = input("Title: ")
file.write("\\title{" + title + "}\n")
author = input("Author: ")
file.write("\\author{" + author + "}\n")
file.write("\\begin{document}\n")
sopUser = input("Would you like sections or paragraphs?(s/p)")

number = int(input("How many?"))

num = range(0, number)

if sopUser == "s" or sopUser == "S":
    for x in num:
        file.write("\\section{Problem " + str(x + 1) + "}\n\n")

if sopUser == "p" or sopUser == "P":
    for x in num:
        file.write("\\paragraph{Problem " + str(x + 1) + "}\n\n")

for x in range(0, number):
    file.write("\\section{Problem " + str(x + 1) + "}\n\n")
    secondary = 0
    secondary = int(input("How many subsections?"))
    char = "a"
    i = ord(char[0])

    for x in range(0, secondary):
        char = chr(i)
        file.write("\\subsection{" + char + ".)}\n\n")
        i += 1
file.write("\\end{document}")
file.close()
