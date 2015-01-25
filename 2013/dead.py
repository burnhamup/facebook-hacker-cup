'''
Created on Feb 2, 2013

@author: Chris
'''

import time

def deadPixels(W,H,P,Q,N,X,Y,a,b,c,d):
    deadList = generateDeadPixels(W,H,N,X,Y,a,b,c,d)
    return searchScreen(W,H,P,Q,deadList)
    
def searchScreen(W,H,P,Q,deadList):
    screenH = H-Q+1
    screenW = W-P+1
    #screen = [[0 for x in xrange(H)] for x in xrange(W)]
    seen = [set() for x in xrange(W)]
    numberOfSpots = screenH * screenW
    for cp in xrange(len(deadList)):
        pixel = deadList[cp]
        #construct search space
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
        #Find a previous point, if any.
        i = cp
        collidedPoint = None
        while i!=0:
            prevPoint = deadList[cp-1]
            if prevPoint[0] < xStart and prevPoint[1] < yStart:
                break
            if prevPoint[0]  < xEnd and prevPoint[1] < yEnd:
                collidedPoint = prevPoint
                break
            i -=1
        if collidedPoint != None:
            pass
        else:
            numberOfSpots -= (xEnd-xStart) * (yEnd-yStart)
        
        if pixel[1] < screenH:
            yEnd = pixel[1]
        for x in xrange(xStart,xEnd+1):            
            for y in xrange(yStart,yEnd+1):
                seen[x].add(y)
    length = 0
    for s in seen:
        length+=len(s)
    return numberOfSpots - length
                    
            
    
    
def generateDeadPixels(W,H,N,X,Y,a,b,c,d):
    first = (X,Y)
    list = []
    list.append(first)
    current = first
    for x in xrange(N-1):
        nextX = (current[0] * a + current[1] * b + 1) % W
        nextY = (current[0] * c + current[1] * d + 1) % H
        current = (nextX,nextY)
        list.append(current)
    list.sort()
    return list


def parseFile(filename):
    f = open(filename)
    numberOfTests = int(f.readline())
    for test in range(numberOfTests):
        (W,H,P,Q,N,X,Y,a,b,c,d) = map(int,f.readline().split())
        result = deadPixels(W,H,P,Q,N,X,Y,a,b,c,d)
        print "Case #"+str(test+1) + ": " + str(result)
start_time = time.time()
# your code
parseFile('input.txt')
elapsed_time = time.time() - start_time
print elapsed_time        