'''
Created on Jan 25, 2013

@author: Chris
'''

def isSmiley(inputText, openParenCount = 0):
    length = len(inputText)
    x = 0
    while x < length:
        if inputText[x] == "(":
            openParenCount+=1
        elif inputText[x] == ")":
            openParenCount -=1
            if openParenCount < 0:
                return False
        elif inputText[x] == ":":
            if x+1 <length:
                if inputText[x+1] in "()":
                    return isSmiley(inputText[x+1:],openParenCount) or isSmiley(inputText[x+2:],openParenCount)
        elif (not (inputText[x].isalpha() or inputText[x] == " ")):
            return False
        x+=1
    return openParenCount == 0


def testStrings():
    assert(isSmiley(":((") == False)
    assert(isSmiley("i am sick today (:()") == True)
    assert(isSmiley("(:)") == True)
    assert(isSmiley("hacker cup: started :):)") == True)
    assert(isSmiley(")(") == False)
    assert(isSmiley("text(moretext)lesstext") == True)
    
def parseFile(filename):
    f = open(filename)
    numberOfTests = int(f.readline())
    for test in range(numberOfTests):
        line = f.readline()
        result = isSmiley(line[:-1])
        if (result):
            output = "YES"
        else:
            output = "NO"
        print "Case #"+str(test+1) + ": " + str(output)
        
testStrings()
parseFile('input.txt')
