from graphics import *

def circles():
    win = GraphWin("Circles", 800, 200)
    win.setBackground('white')
    
    for i in range(15):
        p1 = win.getMouse()
        pX = p1.getX()
        circle = Circle(p1, 20)
        
        if pX < 400:
            circle.setOutline('green')
            if pX < 200:
                circle.setFill('green')
        else:
            circle.setOutline('blue')
            if pX > 600:
                circle.setFill('blue')
        
        circle.draw(win)
    


def circles2():
    win = GraphWin("Circles 2", 800, 200)
    win.setBackground('white')
    
    for i in range(180, 0, -40):
        for j in range(320, 500, 40):
            p1 = win.getMouse()
            pX = p1.getX()
            circle = Circle(Point(j, i), 20)
            
            if pX < 400:
                circle.setOutline('green')
                if pX < 200:
                    circle.setFill('green')
            else:
                circle.setOutline('blue')
                if pX > 600:
                    circle.setFill('blue')
            
            circle.draw(win)
    
    win.getMouse()
    win.close()