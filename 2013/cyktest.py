
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


def CYKParser(Grammar, ipString):

    for row in range(len(ipString)):
    
        # Create string for each column
        ipRow = []
        for col in range(len(ipString) - row):
            st = ipString[col:col + 1 + row]
            ipRow.append(st)
            print st + '\t',
        print
    
        
        # Loop of each ipString
        for col in range(len(ipRow)):
            st = ipRow[col]
            Result = ''
            
            if(len(st) == 1):
                Result = Grammar[st]
                
            elif(len(st) == 2):
                key = ''                
                for i in range(len(st)):
                    key += Grammar[st[i]]
    
                if(Grammar.has_key(key)):
                    Result = Grammar[key]
                    
                # Add grammar
                Grammar[st] = Result
            
            else:
                pre = st[0]
                suf = st[1:]
                pre1 = Grammar[pre]
                suf1 = Grammar[suf]
                set1 = LeftGrammar(pre1, suf1)
                
                pre = st[0:len(st) - 1]
                suf = st[len(st) - 1]
                pre2 = Grammar[pre]
                suf2 = Grammar[suf]
                set2 = LeftGrammar(pre2, suf2)
                
                Result = tuple(set.union(set1, set2))
                
                # Add grammar
                Grammar[st] = Result
        
            ShowResult(Result) 
    
        print
        if row + 1 < len(ipString):
            print '-' * (len(ipString) - row) * (7)


if __name__ == "__main__":

    Grammar = {'AB':('S', 'B'), 'BB':'A', 'a':'A', 'b':'B'}
    ipString = 'aabbabbb'
    CYKParser(Grammar, ipString)