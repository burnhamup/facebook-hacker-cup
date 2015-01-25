'''
Created on Jan 25, 2013

@author: Chris
'''


"""

The algorithim is to take the string. Make everything lowercase, strip out any thing that isn't a letter.
Calculate frequency of each letter. 
Maybe create an array with each index being a different letter and the value is the frequency. Sort this. 
The letter with the highest frequency is 26. This continues on down to 0.
Sum this. Return.

""" 

letters = "abcdefghijklmnopqrstuvwxyz"

def countPretty(prettyString):
    prettyString = ''.join(e for e in prettyString if e.isalpha())
    prettyString = prettyString.lower()
    frequency = {}
    for letter in letters:
        frequency[letter]  = 0
    for letter in prettyString:
        frequency[letter] +=1
    prettyValue = 1
    result = 0
    for freq in sorted(frequency.values()):
        result += freq * prettyValue
        prettyValue +=1
    return result



def testStrings():
    assert(countPretty("ABbCcc") == 152)
    assert(countPretty("Good luck in the Facebook Hacker Cup this year!") ==754)
    assert(countPretty("Ignore punctuation, please :)") == 491)
    assert(countPretty("Sometimes test cases are hard to make up.") == 729)
    assert(countPretty("So I just go consult Professor Dalves") == 646)
    assert(countPretty("abcdefghijklmnopqrstuvwxyz") == 351)
    baseString = ''
    count = 1
    expectedValue = 0
    for x in letters:
        baseString += (x * count)
        expectedValue += (count * count)
        count += 1
    print baseString
    assert(countPretty(baseString) == expectedValue)
    
    
def parseFile(filename):
    f = open(filename)
    numberOfTests = int(f.readline())
    for test in range(numberOfTests):
        result = countPretty(f.readline())
        print "Case #"+str(test+1) + ": " + str(result)
        
testStrings()
#parseFile('input.txt')