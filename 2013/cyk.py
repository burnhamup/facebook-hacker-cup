
'''
@author: Phaisarn Sutheebanjard

CYK Parser
Copyright (C) 2010 - Phaisarn Sutheebanjard

LICENSE
-------
This library is free software; you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free 
Software Foundation; version 2.1 of the License.

This library is distributed in the hope that it will be useful, but WITHOUT 
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more 
details.

You should have received a copy of the GNU Lesser General Public License along
with this library; if not, see <http://www.gnu.org/licenses/>.

For further information contact e-mail: mr.phaisarn@gmail.com

'''


def LeftGrammar(pre, suf):
    Result = []

    for p in pre:
        for s in suf:
            if(Grammar.has_key(p + s)):
                Result.extend(Grammar[p + s])
        
    return set(Result)


def ShowResult(Result):
    Text = '{'
    for res in Result:
        Text += res + ','
    Text = Text.rstrip(',')
    Text += '}\t'
    print Text,
        
#    if (len(Result)==0):
#        print '{}\t',
#    elif (len(Result)==1):
#        print '{%s}\t' % (Result),
#    elif (len(Result)==2):
#        print '{%s,%s}\t' % (Result), 
#    elif (len(Result)==3):
#        print '{%s,%s,%s}\t' % (Result), 
#    elif (len(Result)==4):
#        print '{%s,%s,%s,%s}\t' % (Result), 


def CYKParser(ipString):
    n = len(ipString)
    r = 6
    lookup = {'S':0,'B':1,'C':2,'L':3,'R':4,'X':5}
    P = [[[False for k in xrange(r)] for j in xrange(n)] for i in xrange(n)]
    for i in range(n):
        terminals = Productions[ipString[i]]
        for t in terminals:
            P[i][1][lookup[t]] = True
    for i in range(1,n):
        for j in range(n-i+1):
            for k in range(i-1):
                for ruleKey in Rules:
                    B = lookup[ruleKey[0]]
                    C = lookup[ruleKey[1]]
                    for output in Rules[ruleKey]:
                        A = lookup[output]
                        if P[j][k][B] and P[j+k][i-k][C]:
                            P[j][i][A] = True
    return P[1][n-1][0]
                    
                
        



Productions = {'a': ('S','B'), 'b': ('S','B'), 'c': ('S','B'), 'd': ('S','B'), 'e': ('S','B'), 'f': ('S','B'), 
           'g': ('S','B'), 'h': ('S','B'), 'i': ('S','B'), 'j': ('S','B'), 'k': ('S','B'), 'l': ('S','B'), 
           'm': ('S','B'), 'n': ('S','B'), 'o': ('S','B'), 'p': ('S','B'), 'q': ('S','B'), 'r': ('S','B'), 
           's': ('S','B'), 't': ('S','B'), 'u': ('S','B'), 'v': ('S','B'), 'w': ('S','B'), 'x': ('S','B'), 
           'y': ('S','B'), 'z': ('S','B'), ' ': ('S','B'), ':': ('S','B','C'), ('('): 'L', (')'): 'R', '':('S')}
Rules = {'BR': ('X'), 'CR': ('S','B'), 'CL':('S','B'), 'BB': ('S','B'), 'LX':('S','B'),
           'LR': ('S','B') }
    
def isSmiley(inputString):
    return CYKParser(inputString)

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
        print "Case #"+str(test+1) + ": " + str(result)
        
#isSmiley(":((")
#isSmiley("i am sick today (:()")
#isSmiley('text')
parseFile('input.txt')