import math
from graphics import * 


def circumferenceOfCircle(radius):
    return 2 * math.pi * radius


def areaOfCircle(radius):
    return math.pi * radius ** 2


def circleInfo():
    radius = float(input("What is the radius of your circle? "))
    circumference = circumferenceOfCircle(radius)
    area = areaOfCircle(radius)
    
    print("The area is", round(area, 3), "and the circumference is", 
            round(circumference, 3))

 
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def drawBrownEyeInCentre(centre, radius):
    window = GraphWin("Draw Brown Eye")
    colourList = ['white', 'brown', 'black']
    centre = Point(100, 100)
    radiusList = [60, 30, 15]
    
    for i in range(3):
        drawCircle(window, centre, radiusList[i], colourList[i])
    

def drawBlockOfStars(width, height):
    for i in range(height):
        print('*' * width)


def drawLetterE():
    widthList = [7, 2, 5, 2, 7]
    
    for i in range(5):
        drawBlockOfStars(widthList[i], 2)



def drawBrownEye(win, centre, radius):
    colourList = ['white', 'brown', 'black']
    
    for i in range(3):
        drawCircle(win, centre, radius, colourList[i])
        radius /= 2


def drawPairBrownEyes():
    win = GraphWin("Draw a Pair of Brown Eyes", 640, 640)
    win.setBackground('white')
    
    radius = int(input("What is the radius of your eyes? "))
    print("Now, click where you'd like the left eye")
    centre1 = win.getMouse()
    centre2 = Point(centre1.getX() + radius * 2, centre1.getY())
    centreList = [centre1, centre2]
    
    for i in range(2):
        drawBrownEye(win, centreList[i], radius)


def callToDrawBrownEye():
    win = GraphWin("Draw a Brown Eye", 640, 640)
    win.setBackground('white')
    
    centreX,centreY = input("Enter the X and Y values (max 640, 640) for the "
                                "centre of your eye ").split(" ")
    centre = Point(int(centreX), int(centreY))
    radius = int(input("What is the radius of your eye? "))
    
    drawBrownEye(win, centre, radius)
    
  
def distanceBetweenPoints(p1, p2):
    return math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)


def drawBlocks(spaces1, asterisks1, spaces2, asterisks2, height):
    for i in range(height):
        print(" " * spaces1 + "*" * asterisks1 + " " * spaces2 +
                "*" * asterisks2)

def drawLetterA():
    spaces1 = [1, 0, 0, 0]
    asterisks1 = [8, 2, 10, 2]
    spaces2 = [0, 6, 0, 6]
    asterisks2 = [0, 2, 0, 2]
    height = [2, 2, 2, 3]
    
    for i in range(4):
        drawBlocks(spaces1[i], asterisks1[i], spaces2[i], asterisks2[i],
                    height[i])

def drawFourPairsOfBrownEyes():
    win = GraphWin("Four Eyes", 640, 640)
    win.setBackground('white')
    
    for x in range(2):
        eyeCentre1 = win.getMouse()
        eyeOuter = win.getMouse()
        radius = distanceBetweenPoints(eyeCentre1, eyeOuter)
        
        eyeCentre2 = Point(eyeCentre1.getX() + radius * 2, eyeCentre1.getY())
        centreList = [eyeCentre1, eyeCentre2]
        
        for i in range(2):
            drawBrownEye(win, centreList[i], radius)
    
def displayTextWithSpaces(win, stringInput, pointSize, winPosition):
    stringSpaced = ""
    for i in range(len(stringInput)):
        stringSpaced += stringInput[i] + " "
    
    stringOutput = Text(winPosition, stringSpaced)
    stringOutput.setSize(pointSize)
    stringOutput.draw(win)


def constructVisionChart():
    win = GraphWin("Vision Chart", 640, 640)
    win.setCoords(0.0, 0.0, 12.0, 12.0)
    win.setBackground('white')
    winPositions = [Point(6, 11), Point(6, 9), Point(6, 7), Point(6, 5),\
                    Point(6, 3), Point(6, 1)]
    pointSizes = [30, 25, 20, 15, 10, 5]
    
    for i in range(6):
        stringInput = input("Enter a word ")
        displayTextWithSpaces(win, stringInput.upper(), pointSizes[i], \
                                winPositions[i]) 

def drawStickFigure(win, position, size):
    positionX = position.getX()
    positionY = position.getY()
    head = Circle(position, size)
    head.draw(win)
    body = Line(Point(positionX, positionY + size), \
                Point(positionX, positionY + size * 3))
    body.draw(win)
    arm1 = Line(Point(positionX, positionY + size), \
                Point(positionX - size * 1.5, positionY + size * 2))
    arm1.draw(win)
    arm2 = Line(Point(positionX, positionY + size), \
                Point(positionX + size * 1.5, positionY + size * 2))
    arm2.draw(win)
    leg1 = Line(Point(positionX, positionY + size * 3), \
                Point(positionX - size, positionY + size * 5))
    leg1.draw(win)
    leg2 = Line(Point(positionX, positionY + size * 3), \
                Point(positionX + size, positionY + size * 5))
    leg2.draw(win)

def drawStickFigureFamily():
    win = GraphWin("Draw Stick Figure #3493823", 600, 600)
    
    for i in range(5):
        p1 = win.getMouse()
        p2 = win.getMouse()
        size = distanceBetweenPoints(p1, p2)
        drawStickFigure(win, p1, size)
    
    
    

    
    