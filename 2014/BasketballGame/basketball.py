def game(playerList, minutes, numberOfPlayers):
    leftTeam, rightTeam = draft(playerList)
    leftRoster =rotation(leftTeam, minutes, numberOfPlayers)
    rightRoster = rotation(rightTeam, minutes, numberOfPlayers)
    roster = leftRoster + rightRoster
    roster.sort()
    return roster

def draft(draftables):
    playerList = []
    for line in draftables:
        name, percent, height = line.split()
        percent = int(percent)
        height = int(height)
        playerList.append((name, percent + height / 240.0))
    playerList.sort(key = lambda tup:tup[1], reverse = True)
    leftTeam = []
    rightTeam = []
    for x in range(len(playerList)):
        if x % 2 == 0:
            rightTeam.append(playerList[x])
        else:
            leftTeam.append(playerList[x])
    return leftTeam, rightTeam

def rotation(teamRoster, minutes, numberOfPlayers):
    minutes = minutes % len(teamRoster)
    players = teamRoster[0:numberOfPlayers][::-1] + teamRoster[numberOfPlayers:]
    players += players
    return players[minutes:minutes+numberOfPlayers]


    
    

