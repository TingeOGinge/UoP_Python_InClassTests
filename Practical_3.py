# Practical Worksheet 3: Graphical Programming
# your name, your number

from graphics import *
import math

def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arm1 = Line(Point(100, 80), Point(130, 110))
    arm1.draw(win)
    arm2 = Line(Point(100, 80), Point(70, 110))
    arm2.draw(win)
    leg1 = Line(Point(100, 120), Point(120, 160))
    leg1.draw(win)
    leg2 = Line(Point(100, 120), Point(80, 160))
    leg2.draw(win)
    
drawStickFigure()

def drawLine():
    win = GraphWin("Line drawer")
    message = Text(Point(100,100), "Click on first point")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Click on second point")
    p2 = win.getMouse()
    line = Line(p1, p2)
    line.draw(win)
    message.setText("")
    
def tenLines():
    win = GraphWin("Line drawer", 640, 480)
    message = Text(Point(320, 240), "Click on two points to draw a line")
    message.draw(win)
    for i in range(10):
        p1 = win.getMouse()
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)
    message.setText("Congratulations!")
    
    win.getMouse()
    win.close()
    
#tenLines()

def drawCircle():
    radius = float(input("What is the radius of your circle? "))
    if (radius > 50):
        radius = 50
    win = GraphWin("Draw a Circle", 400, 400)
    win.setCoords(0.0, 0.0, 100.0, 100.0)
    win.setBackground('white')
    centre = Point(50, 50)
    Circle(centre, radius).draw(win)
    
    win.getMouse()
    win.close()
    
#drawCircle()
    

def archeryTarget():
    win = GraphWin("Archery Target", 640, 480)
    win.setBackground('white')
    centre = Point(320, 240)
    colourList = ['blue', 'red', 'yellow']
    radius = 225
    
    for i in range(3):
        circ = Circle(centre, radius)
        radius -= 75
        circ.setFill(colourList[i])
        circ.draw(win)
    
archeryTarget()

def drawRectangle():
    height = float(input("What is the height of your rectangle? "))
    if (height >= 200):
        height = 190
    width = float(input("What is the width of your rectangle? "))
    if (width >= 200):
        width = 190
    
    win = GraphWin("Draw a Rectangle")
    win.setBackground('white')
    heightBuffer = (200 - height) / 2
    widthBuffer = (200 - width) / 2
    
    rect = Rectangle(Point(widthBuffer, heightBuffer), Point(widthBuffer + width, heightBuffer + height))
    rect.setFill('red')
    rect.draw(win)
 
#drawRectangle()


def blueCircle():
    win = GraphWin("Draw a circle", 640, 480)
    p1 = win.getMouse()
    
    circ = Circle(p1, 50)
    circ.setFill('blue')
    circ.draw(win)
    
    win.getMouse()
    win.close()
    
#blueCircle()

def tenStrings():
    win = GraphWin("Ten Strings", 640, 480)
    win.setBackground('white')
    inputText = Entry(Point(320, 50), 20)
    inputText.setText("")
    inputText.draw(win)
    
    for i in range(10):
        p1 = win.getMouse()
        Text(p1, inputText.getText()).draw(win)
    
    win.getMouse()
    win.close()
    
#tenStrings()


def tenRectangles():
    win = GraphWin("Ten Rectangles", 640, 480)
    win.setBackground('white')
    inputText = Entry(Point(320, 50), 20)
    inputText.setText("red")
    inputText.draw(win)
    
    
    for i in range(10):
        # counter = Text(Point(50, 430), 2)
        # counter.setText(i+1)
        # counter.draw(win)
        p1 = win.getMouse()
        p2 = win.getMouse()
        rect = Rectangle(p1, p2)
        rect.setFill(inputText.getText())
        rect.draw(win)
    
    win.getMouse()
    win.close()
    
#tenRectangles()

def fiveClickStickFigure():
    win = GraphWin("Five Click Stick Figure", 640, 480)
    win.setBackground('white')
    
    #Draws the head 
    headCentre = win.getMouse()
    headOuter = win.getMouse()
    radius = math.sqrt((headOuter.getX() - headCentre.getX())**2 + 
                        (headOuter.getY() - headCentre.getY())**2)
    head = Circle(headCentre, radius)
    head.draw(win)
    
    #Draws the body 
    bodyTop = Point(headCentre.getX(),(headCentre.getY() + radius))
    bodyBottom = win.getMouse()
    body = Line(bodyTop, bodyBottom)
    body.draw(win)
    
    #Draws arms
    armsRef = win.getMouse()
    armsOpposite = Point((armsRef.getX() + (bodyTop.getX() - armsRef.getX()) * 2), 
                        armsRef.getY())
    arms = Line(armsRef, armsOpposite)
    arms.draw(win)
    
    #Draws both legs 
    legsBottom = win.getMouse()
    legsDistance = (bodyBottom.getX() - legsBottom.getX()) * 2
    legsTop = bodyBottom
    leg1 = Line(bodyBottom, legsBottom)
    leg2 = Line(bodyBottom, Point((legsBottom.getX() + legsDistance), 
                legsBottom.getY()))
    leg1.draw(win)
    leg2.draw(win)
    
#fiveClickStickFigure()

def plotRainfall():
    win = GraphWin("Plot Rainfall", 320, 240)
    win.setBackground('white')
    win.setCoords(-1.75, -2.0, 8.0, 12.0)
    
    #Creates the input box
    inputText = Entry(Point(3.125, 11.5), 5)
    inputText.setText(" ")
    inputText.draw(win)
    
    #Labels the Y axis
    Text(Point(-1, 0), ' 0mm').draw(win)
    Text(Point(-1, 1), ' 1mm').draw(win)
    Text(Point(-1, 2), ' 2mm').draw(win)
    Text(Point(-1, 3), ' 3mm').draw(win)
    Text(Point(-1, 4), ' 4mm').draw(win)
    Text(Point(-1, 5), ' 5mm').draw(win)
    Text(Point(-1, 6), ' 6mm').draw(win)
    Text(Point(-1, 7), ' 7mm').draw(win)
    Text(Point(-1, 8), ' 8mm').draw(win)
    Text(Point(-1, 9), ' 9mm').draw(win)
    Text(Point(-1, 10), '10mm').draw(win)
    
    #Creates the bar for each day, labelling the x-axis as it goes 
    day = 0
    while (day < 7):
        marker = win.getKey()
        if (marker == 'Return'):
            bar = Rectangle(Point(day,0), 
                            Point(day + 1, float(inputText.getText())))
            bar.setFill("green")
            bar.setWidth(2)
            bar.draw(win)
            Text(Point((day + 0.5), -1), "Day " + str(day+1)).draw(win)
            day += 1
    
#plotRainfall()
    