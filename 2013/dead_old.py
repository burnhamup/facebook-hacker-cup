'''
Created on Feb 2, 2013

@author: Chris
'''

def deadPixels(W,H,P,Q,N,X,Y,a,b,c,d):
    deadList = generateDeadPixels(W,H,N,X,Y,a,b,c,d)
    return searchScreen(W,H,P,Q,deadList)
    
def searchScreen(W,H,P,Q,deadList):
    screenH = H-Q+1
    screenW = W-P+1
    screen = [[0 for x in xrange(H)] for x in xrange(W)]
    numberOfSpots = screenH * screenW
    for pixel in deadList:
        if pixel[0] >= W or pixel[1] >= H or screen[pixel[0]][pixel[1]] == 2:
            continue #This pixel has been seen before
        else:
            screen[pixel[0]][pixel[1]] = 2
            if pixel[0] < screenW and pixel[1] < screenH:
                numberOfSpots-=1
            xStart = 0
            if pixel[0]-P+1 > 0:
                xStart = pixel[0]-P+1
            xEnd = screenW-1
            if pixel[0] < screenW:
                xEnd = pixel[0]
            yStart = 0
            if pixel[1] - Q + 1 > 0:
                yStart = pixel[1] -Q +1
            yEnd = screenH-1
            if pixel[1] < screenH:
                yEnd = pixel[1]
            for x in xrange(xStart,xEnd+1):            
                for y in xrange(yStart,yEnd+1):
                    if screen[x][y] != 2:
                        if screen[x][y] == 0:
                            screen[x][y] = 1
                            numberOfSpots -=1
    return numberOfSpots
                    
            
    
    
def generateDeadPixels(W,H,N,X,Y,a,b,c,d):
    first = (X,Y)
    list = set()
    list.add(first)
    current = first
    for x in xrange(N-1):
        nextX = (current[0] * a + current[1] * b + 1) % W
        nextY = (current[0] * c + current[1] * d + 1) % H
        current = (nextX,nextY)
        list.add(current)
    return list


def parseFile(filename):
    f = open(filename)
    numberOfTests = int(f.readline())
    for test in range(numberOfTests):
        (W,H,P,Q,N,X,Y,a,b,c,d) = map(int,f.readline().split())
        result = deadPixels(W,H,P,Q,N,X,Y,a,b,c,d)
        print "Case #"+str(test+1) + ": " + str(result)
        
parseFile('input.txt')