from graphics import *

def drawOnWhiteboard(win):
    letters = 'abcdefgh'
    win.getMouse()
    
    for i in range(8):
        letterOutput = Text(Point(210, 100), letters[i])
        letterOutput.setTextColor('blue')
        letterOutput.setSize(30)
        letterOutput.draw(win)
        win.getMouse()
        if i < 7:
            letterOutput.undraw()

def teacher():
    win = GraphWin("Stick figure", 300, 200)
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(70, 90), Point(130, 90))
    arms.draw(win)
    leg1 = Line(Point(100, 120), Point(80, 170))
    leg1.draw(win)
    leg2 = Line(Point(100, 120), Point(120, 170))
    leg2.draw(win)

    whiteboard = Rectangle(Point(140, 50), Point(280, 150))
    whiteboard.setFill('white')
    whiteboard.draw(win)
    
    marker = Rectangle(Point(119, 100), Point(126, 80))
    marker.setFill('black')
    marker.draw(win)
    
    markerTip = Rectangle(Point(121, 80), Point(124, 75))
    markerTip.setFill('blue')
    markerTip.draw(win)
    
    drawOnWhiteboard(win)
    markerTip.setFill('white')

teacher()