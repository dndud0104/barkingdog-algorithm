s = "PAYPALISHIRING"
numRows = 2

def solutions(s,numRows):
    if numRows == 1:
        return s

    arr = []
    direction = 0
    point = 0
    for word in s:
        arr.append([word,point])
        if direction == 0:
            point+=1
        elif direction == 1:
            point-=1

        if point == numRows:
            point-=2
            direction = 1
        if point == 0:
            direction = 0

    arr = sorted(arr,key=lambda x:x[1])
    answer = ""
    for a in arr:
        answer+=a[0]
    return answer
            



print(solutions(s, numRows))


#통과하지만 매우 비효율
##def solutions(s, numRows):
##    if numRows == 1:
##        return s
##    
##    paper = [[""]*numRows for _ in range(len(s))]
##    answer = ""
##
##    countRow = 0
##    countCol = 0
##    direction = 0
##    for word in s:
##        paper[countRow][countCol] = word
##        if direction == 0:
##            countCol += 1
##        elif direction == 1:
##            countCol -= 1
##            countRow += 1
##        
##
##        if countCol == numRows:
##            countRow += 1
##            direction = 1
##            countCol -= 2
##        if countCol == 0:
##            direction = 0
##        
##        
##
##    for x in paper:
##        print(x)
##    
##    tmp = [list(x) for x in zip(*paper)]
##    for x in tmp:
##        answer+="".join(x)
##            
##    return answer
