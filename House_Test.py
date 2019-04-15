#-------------------------------------------------------------------------------
# house.py - a simple program to draw a house
#-------------------------------------------------------------------------------

from graphics import *

def main():
    doorColour, doorNumber, lightsOn, winSize = getInputs()
    drawHouse(doorColour, doorNumber, lightsOn, winSize)

def getInputs():
    doorColour = input("Enter door colour: ")
    doorNumber = input("Enter door number: ")
    lightsYN = input("Are the lights on (y/n): ")
    lightsOn = lightsYN[0].lower() == "y"
    winSize = float(input("Enter length of GraphWin size "))
    return doorColour, doorNumber, lightsOn, winSize

def drawHouse(doorColour, doorNumber, lightsOn, winSize):
    win = GraphWin("House", winSize, winSize)
    win.setCoords(0.0, 200.0, 200.0, 0.0)

    roof = Polygon(Point(2, 60), Point(42, 2),
                   Point(158, 2), Point(198,60))
    roof.setFill("pink")
    roof.draw(win)

    # draw wall, door and door number
    drawRectangle(win, Point(2, 60), Point(198, 198), "brown")
    drawRectangle(win, Point(30, 110), Point(80, 198), doorColour)
    numberSign = Text(Point(55, 122), doorNumber).draw(win)
    numberSign.setSize(20)
    

    # draw window
    if lightsOn:
        windowColour = "yellow"
    else:
        windowColour = "black"
    drawRectangle(win, Point(110, 110), Point(170, 170), windowColour)
    
def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)

main()
