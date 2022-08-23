from collections import deque


dx = [1,0,-1,0]
dy = [0,1,0,-1]


def bfs():
    R, C = map(int, input().split()) #가로, 세로
    mage = []
    for i in range(C):
        row = input()
        mage.append([a for a in row])

##    R = 4
##    C = 3
##    mage = [['#','#','#','#'],
##            ['#','*','@','.'],
##            ['#','#','#','#']]
    

    distF = [[-1]*R for i in range(C)]
    distS = [[-1]*R for i in range(C)]

    queF = deque([])
    queS = deque([])

    for i in range(C):
        for j in range(R):
            if mage[i][j] == '*':
                queF.append([i,j])
                distF[i][j] = 0
            elif mage[i][j] == '@':
                queS.append([i,j])
                distS[i][j] = 0

        
    while queF:
        xy = queF.popleft()
        for index in range(4):
            x = xy[0] + dx[index]
            y = xy[1] + dy[index]
            if x < 0 or x >= C or y < 0 or y >= R:
                continue
            if mage[x][y] == '#' or distF[x][y] >= 0:
                continue
            distF[x][y] = distF[xy[0]][xy[1]] + 1
            queF.append([x,y])

    while queS:
        xy = queS.popleft()
        for index in range(4):
            x = xy[0] + dx[index]
            y = xy[1] + dy[index]
            if x < 0 or x >= C or y < 0 or y >= R:
                return distS[xy[0]][xy[1]] + 1
            if mage[x][y] == '#' or distS[x][y] >= 0:
                continue
            if distF[x][y] != -1 and distF[x][y]<=distS[xy[0]][xy[1]]+1:
                continue
            distS[x][y] = distS[xy[0]][xy[1]] + 1
            queS.append([x,y])
    
    return 'IMPOSSIBLE'



T = int(input()) #테스트케이스 수
##T = 1
for i in range(T):
    print(bfs())

