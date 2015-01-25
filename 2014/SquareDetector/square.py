
def hasSquare(field):
    #Find First Black cell.
    #Find out how many black cells are in that row
    #Verify that there is a square formed from that row.
    col = 0
    foundStart = False
    rowLength = 0
    
    for row in field:
        col = 0
        if not foundStart:
            for cell in row:
                if cell == "#":
                    if not foundStart:
                        startCol = col
                        rowLength = 1
                        foundStart = True
                    else:
                        rowLength += 1
                        
                col += 1
            if foundStart:
                checkedRows = rowLength
        else:
            checkedRows -= 1
            for cell in row:
                if checkedRows > 0:
                    if cell == '#' and (col < startCol or col >= startCol + rowLength):
                        return False
                    if cell != '#' and (col >= startCol and col < startCol + rowLength):
                        return False
                else:
                    if cell == '#':
                        return False
                col +=1
    return True
                
                    
    #I have the start cell, length, etc..
    
                
                    
                 
    
