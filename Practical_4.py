
from graphics import *
import os

# os.getcwd() generates the current working directory into a string
# os.chdir() changes the directory
# os.listdir() shows the file in the directory
#you can specify in which folder using a string literal 


def personalGreeting():
    name = input("What is your name? ")
    print("Hello", name.title() + ", nice to see you!")
    
#personalGreeting()


def formalName():
    firstName, lastName = input("What is your first and last name? ").split(" ")
    print(firstName[0].title() + ".", lastName.title())
    
#formalName()


def kilos2pounds():
    kilos = float(input("Enter a weight in kilograms: "))
    pounds = 2.2 * kilos
    print("{0:4.2f} kilos is equal to {1:4.2f} pounds".format(kilos, pounds))
    
#kilos2pounds()


def generateEmail():
    firstName, lastName, firstYear = input("Enter your first name, last name " +
                                "and year you started university:\n").split(" ")
    
    email = lastName[:4].lower() + "." + firstName[0].lower() + "." + \
            firstYear[2:] + "@myport.ac.uk"
    print(email)

#generateEmail()


def gradeTest():
    testResult = int(round(float(input("How many marks did you get on your test? "))))
    if testResult > 10:
        print("Error: there were only 10 test marks available")
    else:
        gradeString = 'FFFFCCBBAAA'
        print("You acheived a grade of:", gradeString[testResult])
    
#gradeTest()


def graphicLetters():
    userString = input("Please enter any word ")
    win = GraphWin("Graphic Letters", 640, 480)
    win.setBackground('white')
    
    for i in range(len(userString)):
        position = win.getMouse()
        letter = Text(position, userString[i])
        letter.setSize(35)
        letter.draw(win)

#graphicLetters()


def singASong():
    songWord, lineIterator, wordIterator = input("Enter your word the number "
                    "of lines and the number of repititions per line\n").split()
    lineIterator = int(lineIterator)
    wordIterator = int(wordIterator)
    
    for i in range(lineIterator):
        print((songWord + " ") * wordIterator)

#singASong()


def exchangeTable():
    win = GraphWin("Exchange Table", 640, 640)
    win.setBackground('white')
    win.setCoords(0.0, -2.0, 4.0, 25.0)
    
    title = Text(Point(2, 23), "Exchange Table")
    title.setSize(25)
    title.draw(win)
    Text(Point(1, 21), "Euros").draw(win)
    Text(Point(3, 21), "Pounds").draw(win)
    
    for i in range(21):        
        Text(Point(1, 20 - i), "{0:2}".format(i)).draw(win)
        Text(Point(3, 20 - i), "{0:5.2f}".format(i / 1.09)).draw(win)
    
#exchangeTable()


def makeAcronym():
    # words = input("Enter your string to receive its acronym\n").split(" ")
    # for i in range(len(words)):
    #     print(words[i][0].upper(), end="")
    
    
    win = GraphWin("Make an Acronym", 640, 480)
    win.setBackground('white')
    win.setCoords(0.0, 0.0, 12.0, 9.0)
    
    inputText = Entry(Point(6, 6), 30)
    inputText.setText("")
    inputText.draw(win)
    Text(Point(6, 5), "Enter your text to get your acronym").draw(win)
    
    while(win.getKey() != 'Return'):
        acronym = ""
    words = inputText.getText()
    words = words.split()
    for i in range(len(words)):
        acronym += words[i][0].upper()
    Text(Point(6, 3), acronym).draw(win)

#makeAcronym()


def nameToNumber():
    
    name = input("Please enter your name ").split(" ")
    nameNumericValue = 0
    
    for i in range(len(name)):
        for j in range(len(name[i])):
            nameNumericValue += ord(name[i][j].lower()) - 96

    print("The numeric value of your name is", nameNumericValue)
    
#nameToNumber()


def fileInCaps():
    os.chdir("C:/Users/dillo/Documents/University/Introduction to Programming/"
                "Main/Module 1/")
    fileName = input("What is the name of your file? ")
    inFile = open(fileName, "r")
    fileContents = inFile.read()
    inFile.close()
    
    print(fileContents.upper())
    
#fileInCaps()

def rainfallChart():
    inFile = open("rainfall.txt", "r")
    rainfallData = inFile.readlines()
    inFile.close()
    
    for line in rainfallData:
        parts = line.split(" ")
        print("{0:12}".format(parts[0]), "*" * int(parts[1]))
    
#rainfallChart()
    

def graphicalRainfallChart():
    win = GraphWin("Plot Rainfall", 640, 480)
    win.setBackground('white')
    win.setCoords(-2.0, -5.0, 10.0, 55)
    title = Text(Point(4, 50), "Rainfall Chart")
    title.setSize(25)
    title.draw(win)
    
    inFile = open("rainfall.txt", "r")
    rainfallData = inFile.readlines()
    inFile.close()
    
    for i in range(0, 50, 5):
        Text(Point(-1, i), "{0:2}".format(i) + "mm -").draw(win)
    
    xLabel = 0
    for lines in rainfallData:
        parts = lines.split()
        Text(Point(xLabel + 0.5, -2.5), parts[0][0:4].upper()).draw(win)
        bar = Rectangle(Point(xLabel, 0), Point(xLabel + 1, int(parts[1])))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
        xLabel += 1

#graphicalRainfallChart()


def rainfallInInches():
    inFile = open("rainfall.txt", "r")
    rainfallData = inFile.readlines()
    inFile.close()
    
    outFile = open("rainfallInInches.txt", "w")
    for lines in rainfallData:
        values = lines.split()
        print("{0:10}\t{1:4.2f}".format(values[0], float(values[1]) / 25.4), 
                file=outFile)
    
    outFile.close()

#rainfallInInches()


def wc():
    filename = input("What is the name of your file? ")
    
    inFile = open(filename, "r")
    fileLines = inFile.readlines()
    inFile.close()
    totalChars = 0
    totalWords = 0
    totalLines = len(fileLines)
    for line in fileLines:
        totalChars += len(line)
        line = line.split()
        totalWords += len(line)
    
    print("Char count =\t{0:<10}\n".format(totalChars) +
            "Word count =\t{0:<10}\n".format(totalWords) +
            "Line count =\t{0:<10}".format(totalLines))

#wc()