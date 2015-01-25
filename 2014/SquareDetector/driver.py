import square
def parseFile(filename):
    f = open(filename)
    numberOfTests = int(f.readline())
    for test in range(numberOfTests):
        numberOfLines = int(f.readline())
        list = []
        for line in range(numberOfLines):
            list.append(f.readline())
        
        if square.hasSquare(list):
            result = "Yes"
        else :
            result = "No"
        print "Case #"+str(test+1) + ": " + result

parseFile('input.txt')