
import collections 
import time
def createList(a,b,c,r,k):
    m=[]
    m.append(a)
    prev = a
    for i in range(1,k):
        prev = (b * prev +c) % r
        m.append(prev)
    return m

def driver(n,k,a,b,c,r):
    m = createList(a,b,c,r,k)
    return calculate(m,n,k)

def calculate(m,n,k):
    possibleValues = [0 for x in range(k+1)]
    queue = collections.deque()
    for x in m:
        if x <= k:
            possibleValues[x] +=1
        queue.append(x)
    searchStart = 0
    x = k
    while x <n and x < 2*k:
        #Find Minimum value
        minValue = searchStart
        while possibleValues[minValue]:
            minValue+=1
        #Append value to m
        queue.append(minValue)
        #Set new value to true
        possibleValues[minValue] +=1
        #set departing value to false
        oldValue = queue.popleft()
        searchStart = minValue
        if oldValue <= k:
            possibleValues[oldValue] -=1
            if oldValue < minValue and possibleValues[oldValue] == 0:
                searchStart = oldValue
        x+=1
    if x == 2*k:
        return queue[(n-x-2)%(k+1)]
    return minValue
    
def test():
    assert(driver(97,39,34,37,656,97) == 8)
    assert(driver(186,75,68,16,539,186) == 38)
    assert(driver(137,49,48,17,461,137) == 41)
    assert(driver(98,59,6,30,524,98) == 40)
    assert(driver(46,18,7,11,9,46) == 12)

def parseFile(filename):
    f = open(filename)
    numberOfTests = int(f.readline())
    for test in range(numberOfTests):
        (n,k) = f.readline().split()
        (a,b,c,r) = f.readline().split()
        result = driver(int(n),int(k),int(a),int(b),int(c),int(r))
        print "Case #"+str(test+1) + ": " + str(result)
test()
parseFile('input.txt')


    