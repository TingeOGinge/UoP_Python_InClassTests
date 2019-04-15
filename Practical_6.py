#-------------------------------------------------------------------------------
# Practical Worksheet 6: if statements and for loops
# Dillon O'Shea
# 887062
#-------------------------------------------------------------------------------

from graphics import *
import math
import random

# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

# For exercise 8 
def drawColouredEye(win, centre, radius, colour):
    colourList = ['white', colour, 'black']
    
    for i in range(3):
        drawCircle(win, centre, radius, colourList[i])
        radius /= 2

def eyePicker():
    win = GraphWin("Eye Picker", 600, 600)
    
    for i in range(5):
        print("Please click on the screen where you would like your eye to be ")
        centre = win.getMouse()
        radius, colour = input("Now enter the radius and colour of your eye "
                                ).split()
        colourList = ['blue', 'grey', 'green', 'brown']
        radius = int(radius)
        colour = colour.lower()
        if colour in colourList:
                drawColouredEye(win, centre, radius, colour)
        else:
            print("{0} is not a valid eye colour".format(colour))
    
#eyePicker()

def fastFoodOrderPrice():
    orderPrice = float(input("What is the base price of your order? "))
    if orderPrice < 10:
        orderPrice += 1.5
    
    print("The total cost of your order = £{0:.2f}".format(orderPrice))


def whatToDoToday():
    temperature = float(input("What is the temperature today? "))
    if temperature > 25:
        print("Get in the fucking sea, ya cunt")
    elif temperature <= 25 and temperature >= 10:
        print("For a less 'hobo sheek' look, try Gunwharf, you scruffy wanker")
    elif temperature < 10:
        print("It's cold, you should read a book. Assuming you can read, "
                "you absolute cockwomble ")


def displaySquareRoots(start, end):
    
    for i in range(start, end + 1):
        print("The sqaure root of {0} is {1:.3f}".format(i, math.sqrt(i)))


def calculateGrade(mark):
    if mark <=20 and mark >= 16:
        return 'A'
    elif mark < 16 and mark >= 12:
        return 'B'
    elif mark < 12 and mark >= 8:
        return 'C'
    elif mark < 8 and mark >= 0: 
        return 'F'
    else:
        return 'X'

def teacher():
    score = int(input("What score did you receive?\n"))
    print("{0:2} = {1}".format(score, calculateGrade(score)))


def peasInAPod():
    numOfPeas = int(input("How many peas are in the pod?\n"))
    radius = 50
    diameter = radius * 2
    win = GraphWin("Peas In A Pod", numOfPeas * diameter, diameter)
    
    peaCentre = Point(radius, radius)
    for i in range(numOfPeas):
        pea = Circle(peaCentre, radius)
        pea.setFill('green')
        pea.draw(win)
        peaCentre.move(diameter, 0)


def ticketPrice(distance, age):
    base = 3
    costPerKm = 0.15
    price = base + costPerKm * distance
    if age >= 60 or age <= 15:
        price *= 0.6
    return price 

def trainJourney():
    distance, age = input("Enter the distance and your age\n").split()
    distance = float(distance)
    age = int(age)
    
    print("The total cost of your journey = £{0:.2f}"\
            .format(ticketPrice(distance, age)))


def numberedSquare(number):
    for i in range(number, 0, -1):
        for j in range(i, i + number):
            print("{0:<2}".format(j), end=" ")
        print("\n")


def drawPatchWindow():
    win = GraphWin("Patch 2")
    win.setBackground('white')
    win.setCoords(0.0, 20.0, 20.0, 0.0)
    
    for i in range(1, 10, 2):
        for j in range(1, 10, 2):
            hiBox = Text(Point(i, j), "hi!")
            hiBox.setTextColor('red')
            #hiBox.setSize(15)
            hiBorder = Rectangle(Point(j - 1, i - 1), Point(j + 1, i + 1))
            hiBorder.setOutline('red')
            hiBorder.draw(win)
            hiBox.draw(win)

#drawPatchWindow()


def drawPatch(win, xCoord, yCoord, colour):
    
    for i in range(yCoord + 10, yCoord + 100, 20):
        for j in range(xCoord + 10, xCoord + 100, 20):
            hiBox = Text(Point(j, i), "hi!")
            hiBox.setTextColor(colour)
            hiBox.setSize(8)
            hiBorder = Rectangle(Point(j - 10, i - 10), Point(j + 10, i + 10))
            hiBorder.setOutline(colour)
            hiBorder.draw(win)
            hiBox.draw(win)

def drawPatchwork():
    win = GraphWin("Draw Patch Work", 300, 200)
    
    for i in range(0, 200, 100):
        for j in range(0, 300, 100):
            drawPatch(win, j, i, 'red')

#drawPatchwork()

def eyesAllAround():
    win = GraphWin("Eyes All Around", 500, 500)
    colourList = ['blue', 'grey', 'green', 'brown']
    radius = 30
    
    for i in range(30):
        centre = win.getMouse()
        j = i % 4
        drawColouredEye(win, centre, radius, colourList[j])

#eyesAllAround()

def distanceBetweenPoints(p1, p2):
    return math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)

def archeryTarget(win):
    centre = Point(320, 240)
    colourList = ['blue', 'red', 'yellow']
    radius = 225
    
    for i in range(3):
        circ = Circle(centre, radius)
        radius -= 75
        circ.setFill(colourList[i])
        circ.draw(win)

def generateAtmos():
    return random.randint(-100, 100)
    
def arrowFlux():
    return random.randint(-35, 35)

def generateScore(offTarget):
        if offTarget <= 75:
            return 10
        elif offTarget > 75 and offTarget <= 150:
            return 5
        elif offTarget > 150 and offTarget <= 225:
            return 2
        else:
            return 0

def shootArrow(win, horizontal, vertical):
        p1 = win.getMouse()
        p1.move(horizontal, vertical)
        arrow = Line(p1, Point(p1.getX() - arrowFlux(), p1.getY() + 100))
        arrow.setWidth(3)
        arrow.setArrow('first')
        arrow.draw(win)
        return p1

def initialiseUI(win):
    horizontalDisplay = Text(Point(55, 50), " ")
    verticalDisplay = Text(Point(55, 100), " ")
    scoreDisplay = Text(Point(50, 400), " ")
    scoreDisplay.draw(win)
    horizontalDisplay.draw(win)
    verticalDisplay.draw(win)
    score = 0
    
    return horizontalDisplay, verticalDisplay, scoreDisplay, score

def updateUI(score, scoreDisplay, horizontalDisplay, verticalDisplay, i):
    scoreDisplay.setText("Score: {0}".format(score))
    if i < 4:
        horizontal = generateAtmos()
        vertical = generateAtmos()
        horizontalDisplay.setText("Horizontal: {0:4}".format(horizontal))
        verticalDisplay.setText("  Vertical: {0:4}".format(vertical))
        return horizontal, vertical
    else:
        return 0, 0
    

def archeryGame():
    win = GraphWin("Archery Game", 640, 480)
    win.setBackground('white')
    archeryTarget(win)
    horizontalDisplay, verticalDisplay, scoreDisplay, score = initialiseUI(win)
    horizontal, vertical = updateUI(score, scoreDisplay, horizontalDisplay, 
                                        verticalDisplay, 0)
    
    for i in range(5):
        p1 = shootArrow(win, horizontal, vertical)
        #offTarget = 
        BetweenPoints(Point(320, 240), p1)
        score += generateScore(offTarget)
        horizontal, vertical = updateUI(score, scoreDisplay, horizontalDisplay, 
                                            verticalDisplay, i)

#archeryGame()


def drawPatchZero():
    win = GraphWin("Patch 0")
    win.setBackground('white')
    
    for i in range(0, 200, 20):
        lines1 = Line(Point(i, 0), Point(200, i + 20))
        lines1.setOutline('red')
        lines1.draw(win)
        lines2 = Line(Point(0, i), Point(i + 20, 200))
        lines2.setOutline('red')
        lines2.draw(win)
    

    

def drawPatchOne():
    win = GraphWin("Patch 1")
    win.setBackground('white')
    
    for i in range(0, 201, 20):
        lines1 = Line(Point(i, 0), Point(200 - i, 200))
        lines1.setOutline('red')
        lines1.draw(win)
        
        lines2 = Line(Point(0, i), Point(200, 200 - i))
        lines2.setOutline('red')
        lines2.draw(win)


def drawPatchTwo():
    win = GraphWin("Patch 2")
    win.setBackground('white')
    win.setCoords(0.0, 10.0, 10.0, 0.0)
    
    for i in range(1, 10, 2):
        for j in range(1, 10, 2):
            hiBox = Text(Point(i, j), "hi!")
            hiBox.setTextColor('red')
            #hiBox.setSize(15)
            hiBorder = Rectangle(Point(j - 1, i - 1), Point(j + 1, i + 1))
            hiBorder.setOutline('red')
            hiBorder.draw(win)
            hiBox.draw(win)


def drawPatchThree():
    win = GraphWin("Patch 3")
    win.setBackground('white')
    colourList = ['red', 'white', 'red', 'white', 'red']
    colourListIndex = 0 
    
    for i in range(20, 200, 40):
        for j in range(20, 200, 40):
            circles = Circle(Point(j, i), 20)
            circles.setFill(colourList[colourListIndex])
            circles.setOutline('red')
            circles.draw(win)
        colourListIndex += 1




def drawPatchFour():
    win = GraphWin("Patch 4")
    win.setBackground('white')
    
    for i in range(0, 200, 20):
        rectangles = Rectangle(Point(i, 200 - i), Point(i + 20, 200 - i - 20))
        rectangles.setOutline('red')
        rectangles.setFill('red')
        rectangles.draw(win)




def drawPatchFive(startX, colour):
    win = GraphWin("Patch 5")
    win.setBackground('white')
    
    for i in range(startX, 100, 10):
        rectangles = Rectangle(Point(i, 100 - i), Point(100, 100 - i - 10))
        rectangles.setOutline(colour)
        rectangles.setFill(colour)
        rectangles.draw(win)





def drawPatchSix():
    win = GraphWin("Patch 6")
    win.setBackground('white')
    
    for i in range(10, 200, 20):
        rectangles = Rectangle(Point(i, i), Point(200 - i, 200 - i))
        rectangles.setWidth(9)
        rectangles.setOutline('red')
        rectangles.draw(win)

#drawPatchSix()


def drawPatchSeven():
    win = GraphWin("Patch 6")
    win.setBackground('white')
    radius = 10
    
    for i in range(200, 0, -20):
        circles = Circle(Point(100, 200 - radius), radius)
        circles.setOutline('red')
        circles.draw(win)
        radius += 10




def drawPatchEight():
    win = GraphWin("Patch 7")
    win.setBackground('white')
    
    for i in range(0, 201, 40):
        rightToLeft1 = Line(Point(i, 0), Point(200, 200 - i)).draw(win)
        rightToLeft1.setOutline('red')
        rightToLeft2 = Line(Point(0, i), Point(200 - i, 200)).draw(win)
        rightToLeft2.setOutline('red')
        
        leftToRight1 = Line(Point(0, i), Point(i, 0)).draw(win)
        leftToRight1.setOutline('red')
        leftToRight2 = Line(Point(200 - i, 200), Point(200, 200 - i)).draw(win)
        leftToRight2.setOutline('red')
  




def drawPatchNine(win, startX, startY, colour):
    
    square = Rectangle(Point(startX, startY + 100), 
                                    Point(startX + 10, startY + 90)).draw(win)
    square.setFill(colour)
    square.setOutline(colour)
    
    
    for i in range(20, 100, 20):
        hRectangles = Rectangle(Point(startX, startY + 100 - i), 
                            Point(startX + i, startY + 100 - i - 10)).draw(win)
        hRectangles.setFill(colour)
        hRectangles.setOutline(colour)
        
        vRectangles = Rectangle(Point(startX + i, startY + 100), 
                        Point(startX + i + 10, startY + 100 - i - 10)).draw(win)
        vRectangles.setFill(colour)
        vRectangles.setOutline(colour)

win = GraphWin(" ", 500, 500)
win.setBackground('white')
for y in range(0, 500, 100):
    for x in range(0, 500, 100):
        drawPatchNine(win, x, y, 'blue')

def displayPatches():
    drawPatchZero()
    drawPatchOne()
    drawPatchTwo()
    drawPatchThree()
    drawPatchFour()
    drawPatchFive()
    drawPatchSix()
    drawPatchSeven()
    drawPatchEight()
    drawPatchNine()


#displayPatches()



    
    
    
    