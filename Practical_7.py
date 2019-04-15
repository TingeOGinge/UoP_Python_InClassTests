#-------------------------------------------------------------------------------
# Practical Worksheet 7: Booleans and while loops
# Dillon O'Shea
# 887062
#-------------------------------------------------------------------------------

from graphics import *
import time
from Practical_6 import *

# For exercise 2
def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("black")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        red.setFill('red')
        time.sleep(2)
        amber.setFill('yellow')
        time.sleep(2)
        red.setFill('black')
        amber.setFill('black')
        green.setFill('green')
        time.sleep(2)
        green.setFill('black')
        amber.setFill('yellow')
        time.sleep(2)
        amber.setFill('black')

#trafficLights()

# For exercise 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9, 'C'

def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32, 'F'

def tcUpdateDisplay(temp, unit, total, totalUnit):
    print("{0} {1} is equal to {2:.2f} {3}".format(temp, unit, total, totalUnit))

def temperatureConverter():
    temp = input("Enter your temperature ")
    while True:
        if temp.isdigit() == True:
            temp = float(temp)
            unit = input("Enter the unit of your temperature (F or C) ")
            unit = unit.upper()
            if unit == 'F':
                total, totalUnit = fahrenheit2Celsius(temp)
            elif unit == 'C':
                total, totalUnit = celsius2Fahrenheit(temp)
            else:
                print("Error: Invalid unit entered")
                break
            tcUpdateDisplay(temp, unit, total, totalUnit)
            temp = input("Enter your temperature or N to stop the program ")
        elif temp.upper() == 'N':
            print("Thanks for using me, goodbye!")
            break
        else:
            print("Invalid input")
            temp = input("Enter your temperature or N to stop the program ")
    

def getName():
    while True:
        name = input("What is your name? ")
        if (name.isalpha() == True):
            break
        print("You didn't enter a name!? ")
    return name

#getName()


def gradeCoursework():
    while True:
        mark = input("What mark did the student receive? ")
        if mark.isdigit() == True:
            mark = int(mark)
            if mark >= 0 and mark <= 20:
                grade = calculateGrade(mark)
                break
        print("Invalid input: Please enter the student's mark")
    print("The pupil acheived a grade of {0}".format(grade))


def orderPrice():
    total = 0
    strCommand = input("Enter the unit price and quantity \n" )
    while strCommand != "":
        strCommandSplit = strCommand.split()
        unitPrice = float(strCommandSplit[0])
        unitQuantity = int(strCommandSplit[1])
        total += unitPrice * unitQuantity
        strCommand = input("Enter the unit price and quantity to continue \n"
                            "Hit enter to quit and see your total \n")
    
    print("The total cost of your order = £{0:.2f}".format(total))


def clickableEye():
    win = GraphWin("Clickable Eye", 640, 480)
    win.setBackground('white')
    centre = Point(320, 240)
    drawColouredEye(win, centre, 100, 'brown')
    eyePartDisplay = Text(Point(320, 360), "")
    eyePartDisplay.draw(win)
    
    while True:
        p1 = win.getMouse()
        dist = distanceBetweenPoints(p1, centre)
        if dist <= 25:
            eyePart = 'pupil'
        elif dist > 25 and dist <= 50:
            eyePart = 'iris'
        elif dist > 50 and dist <= 100:
            eyePart = 'sclera'
        else:
            break
        eyePartDisplay.setText("You clicked on the {0}".format(eyePart))
    win.close()

#clickableEye()


def guessTheNumber():
    isAWinner = False
    answer = random.randint(1, 100)
    print("I'm thinking of an integer between 1 - 100, you have 7 guesses")
    for i in range(1, 8):
        print("Guess {0}:".format(i), end=" ")
        guess = int(input("Enter your guess \n"))
        if guess < answer:
            print("Too low")
        elif guess > answer:
            print("Too high")
        else:
            isAWinner = True
            break
    if isAWinner == True:
        print("You win! It took {0} attempt(s)".format(i))
    else:
        print("You lose! The correct answer was {0}".format(answer))
    

    
def tableTennisScorer():
    win = GraphWin("Table Tennis Scorer", 640, 480)
    win.setBackground('white')
    Line(Point(320, 0), Point(320, 480)).draw(win)
    leftPlayer = 0
    rightPlayer = 0 
    leftDisplay = Text(Point(160, 240), "0")
    leftDisplay.setSize(36)
    leftDisplay.draw(win)
    rightDisplay = Text(Point(480, 240), "0")
    rightDisplay.setSize(36)
    rightDisplay.draw(win)
    
    while True:
        p1 = win.getMouse()
        xPosition = p1.getX()
        
        if xPosition < 320:
            leftPlayer += 1
            leftDisplay.setText(leftPlayer)
        if xPosition > 320:
            rightPlayer += 1
            rightDisplay.setText(rightPlayer)
        
        if leftPlayer >= 11 or rightPlayer >= 11:
            if abs(leftPlayer - rightPlayer) >= 2:
                break
    
    if leftPlayer > rightPlayer:
        winMsg = Text(Point(160, 360), "wins").draw(win)
        winMsg.setSize(36)
    else:
        winMsg = Text(Point(480, 360), "wins").draw(win)
        winMsg.setSize(36)
        
    
    win.getMouse()
    win.close()


#tableTennisScorer()

def drawBoxOfEyes(win, columns, rows, winWidth, winHeight):
    display = Text(Point(winWidth / 2, winHeight - 25), "").draw(win)
    display.setSize(15)
    eyeCentre = Point(100, 100)
    colourList = ['blue', 'red', 'yellow', 'brown']
    centreList = []
    for i in range(rows):
        for j in range(columns):
            drawColouredEye(win, eyeCentre, 50, colourList[random.randint(0,3)])
            centreList.append(eyeCentre)
            eyeCentre.move(100, 0)
        eyeCentre.move(-100 * columns, 100)
    return display
    

def clickableBoxOfEyes():
    columns = int(float(input("How many columns would you like? ")))
    winWidth = columns * 100 + 100 
    rows = int(float(input("How many rows would you like? ")))
    winHeight = rows * 100 + 100
    win = GraphWin("Clickable Box of Eyes", winWidth, winHeight)
    win.setBackground('white')
    Rectangle(Point(50, 50), Point(winWidth - 50, winHeight - 50)).draw(win)
    display = drawBoxOfEyes(win, columns, rows, winWidth, winHeight)
    
    while True:
        p1 = win.getMouse()
        pX = p1.getX()
        pY = p1.getY()
        if pX < 50 or pX > winWidth - 50 or pY < 50 or pY > winHeight - 50:
            win.close()
            break
        col = round(pX / 100)
        row = round(pY / 100)
        dist = distanceBetweenPoints(p1, Point(col * 100, row * 100))
        if dist <= 50:
            display.setText("Eye at row {0}, column {1}".format(row, col))
        else:
            display.setText("Between eyes")

#clickableBoxOfEyes()


def ftcInitialiseUI(win):
    scoreDisplay = Text(Point(20, 460), "").draw(win)
    scoreDisplay.setSize(20)
    progressDisplay = Text(Point(320, 460), "Click on the circle, if you can!"
                            ).draw(win)
    progressDisplay.setSize(20)
    score = 0
    return scoreDisplay, progressDisplay, score

def createCircle(win, radius):
    colourList = ['blue', 'red', 'yellow', 'brown']
    radius = int(radius)
    x = random.randint(radius, 640 - radius)
    y = random.randint(radius, 480 - radius)
    circle = Circle(Point(x, y), radius)
    circle.setFill(colourList[random.randint(0, 3)])
    return circle


def findTheCircle():
    win = GraphWin("Find The Circle", 640, 480)
    win.setBackground('white')
    scoreDisplay, progressDisplay, score = ftcInitialiseUI(win)
    radius = 30 
    keepPlaying = True
    
    while keepPlaying == True:
        circle = createCircle(win, radius)
        centre = circle.getCenter()
        p1 = win.getMouse()
        for i in range(10, 0, -1):
            dist = distanceBetweenPoints(p1, centre)
            if dist <= radius:
                score += i 
                scoreDisplay.setText(str(score))
                progressDisplay.setText("You win! Click to play again")
                circle.draw(win)
                
                win.getMouse()
                circle.undraw()
                progressDisplay.setText("Click on the circle, if you can!")
                radius *= 0.9
                break
            if i == 1:
                keepPlaying = False
                progressDisplay.setText("You lose! :(")
                circle.draw(win) 
                break
            elif i < 10 and i > 1:
                if dist < prevDist:
                    progressDisplay.setText("Getting closer")
                elif dist > prevDist:
                    progressDisplay.setText("Getting further away")
                else:
                    progressDisplay.setText("Exactly the same distance away")
            prevDist = dist
            p1 = win.getMouse()
    
    
    
    
    
    
    
    
    
    
    
