import basketball
def parseFile(filename):
    f = open(filename)
    numberOfTests = int(f.readline())
    for test in range(numberOfTests):
        totalPlayerCount, minutes, numberOfPlayers  = map(int, f.readline().split())
        
        playerList = []
        for line in range(totalPlayerCount):
            playerList.append(f.readline())
        currentRoster = basketball.game(playerList,minutes, numberOfPlayers)
        result = ""
        for player in currentRoster:
            result += " " + player[0]
        print "Case #"+str(test+1) + ":" + result 

parseFile('input.txt')