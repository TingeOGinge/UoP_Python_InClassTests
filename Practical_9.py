from graphics import *

def displayDate(day, month, year):
    monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug', 'Sept',\
                    'Oct', 'Nov', 'Dec']
    if day > 3:
        suffix = 'th'
    else:
        if day == 1:
            suffix = 'st'
        elif day == 2:
            suffix = 'nd'
        elif day == 3:
            suffix = 'rd'
        
    print("{0}{1} {2} {3}".format(day, suffix, monthList[month - 1], year))

#displayDate(14, 2, 2011)

def wordLengths(wordList):
    for i in range(len(wordList)):
        print("{0} {1}".format(wordList[i], len(wordList[i])))

#wordLengths(['bacon', 'jam', 'spam'])

def drawHexagon():
    win = GraphWin("Draw Hexagon", 400, 400)
    win.setBackground('white')
    hexPointList = []
    
    for i in range(6):
        p = win.getMouse()
        hexPointList.append(p)
    
    hex = Polygon(hexPointList).draw(win)
    hex.setFill('red')
    
#drawHexagon()

def testMarks():
    topMark = 10
    markList = []
    resultList = [0] * (topMark + 1)
    mark = " "
    while mark != "":
        mark = input("Enter the student's mark or hit enter now to continue ")
        if mark.isdigit() == True:
            mark = int(mark)
            markList.append(mark)
    
    for i in markList:
        if i <= topMark and i >= 0:
            resultList[i] += 1
            
    for j in range(top mark + 1):
        print("{0} student(s) for {1} mark".format(resultList[j], j))

#testMarks()


def drawBarChart(dataset):
    for i in range(len(dataset)):
        if dataset[i] <= i + 1:
            print()

drawBarChart([3, 2, 1])
    
    
    
    
    
    
    
    
    