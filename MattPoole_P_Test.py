from graphics import * 
from Practical_6 import distanceBetweenPoints

def mattPracticeTest():
    win = GraphWin("Practice Test", 600, 600)
    win.setBackground('white')
    for i in range(200, 401, 200):
        Line(Point(i, 0), Point(i, 600)).draw(win)
    
    for i in range(100, 300, 40):
        for j in range(220, 381, 40):
            p1 = win.getMouse()
            pX = p1.getX()
            colour = 'black'
            
            if pX < 200:
                colour = 'blue'
            elif pX > 200 and pX < 400:
                colour = 'green'
            elif pX > 400:
                colour = 'red'
        
            circles = Circle(Point(j, i), 20).draw(win)
            circles.setFill(colour)
            circles.setOutline(colour)
    

#mattPracticeTest()


def circles():
    win = GraphWin("Circles", 800, 600)
    for i in range(12):
        p1 = win.getMouse()
        pX = p1.getX()
        circle = Circle(p1, 40)
        if pX < 200:
            colour = 'blue'
        elif pX >= 200 and pX < 400:
            colour = 'white'
        elif pX >= 400 and pX < 600:
            colour = 'green'
        elif pX >= 800:
            colour = 'red'
        
        circle.draw(win)







