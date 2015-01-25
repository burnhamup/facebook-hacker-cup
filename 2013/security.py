'''
Created on Feb 2, 2013

@author: Chris
'''

alphabet = ['a','b','c','d','e','f']
def security(k1,k2,m):
    length = len(k1) / m
    possible = []
    actual =[]
    for x in range(m):
        possible.append(k2[x*length:x*length+length])
        actual.append(k1[x*length:x*length+length])
    possibleStrings = matchLists(actual, possible)
    if len(possibleStrings) == 0:
        return "Impossible"
    else:
        possibleStrings.sort()
        print possibleStrings
        return possibleStrings[0]
    
    
def matchLists(k1,k2):
    result = []
    if len(k1):
        piece = k1[0]
        for possible in k2:
            if matchPairs(piece,possible):
                newList = list(k2)
                newList.remove(possible)
                if (len(newList) == 0):
                    currentMatch = enumerateMatchs(piece,possible)
                    result.append(currentMatch)
                else:
                    matches = matchLists(k1[1:], newList)
                    currentMatch = enumerateMatchs(piece,possible)
                    for item in matches:
                            result.append(currentMatch + item)
    return result
            

def matchPairs(string1, string2):
    match = True
    for x in range(len(string1)):
        if not (string1[x] == '?' or string2[x] == '?' or string1[x] == string2[x]):
            match = False
    return match

def enumerateMatchs(string1, string2):
    string1 = list(string1)
    for x in range(len(string1)):
        if string1[x] == '?':
            if  string2[x] == '?':
                string1[x] = 'a'
            else:
                string1[x] = string2[x]
    string1 = ''.join(string1)
    return string1
        

def parseFile(filename):
    f = open(filename)
    numberOfTests = int(f.readline())
    for test in range(numberOfTests):
        m = int(f.readline())
        k1 = f.readline()
        k2 = f.readline()
        result = security(k1,k2,m)
        print "Case #"+str(test+1) + ": " + str(result)


parseFile('input.txt')