from collections import deque

R, C = map(int, input().split())
##R = 4
##C = 4
dx = [1,0,-1,0]
dy = [0,1,0,-1]
count = 0
mage = []
for i in range(R):
    row = input()
    mage.append([a for a in row])
distF = [[-1]*C for i in range(R)]
distJ = [[-1]*C for i in range(R)]
##mage = [['#','#','#','#'],
##        ['#','J','F','#'],
##        ['#','.','.','#'],
##        ['#','.','.','#']]

queF = deque([])
queJ = deque([])

for i in range(len(mage)):
    for j in range(len(mage[i])):
        if mage[i][j] == 'F':
            queF.append([i,j])
            distF[i][j] = 0
        elif mage[i][j] == 'J':
            queJ.append([i,j])
            distJ[i][j] = 0

while queF:
    xy = queF.popleft()
    for index in range(4):
        x = xy[0] + dx[index]
        y = xy[1] + dy[index]
        if x < 0 or x >= R or y < 0 or y >= C:
            continue
        if mage[x][y] == '#' or distF[x][y] >= 0:
            continue
        distF[x][y] = distF[xy[0]][xy[1]] + 1
        queF.append([x,y])

      
while queJ:
    xy = queJ.popleft()
    for index in range(4):
        x = xy[0] + dx[index]
        y = xy[1] + dy[index]
        if x < 0 or x >= R or y < 0 or y >= C:
            print(distJ[xy[0]][xy[1]] + 1)
            exit(0)
        if mage[x][y] == '#' or distJ[x][y] >= 0:
            continue
        if disfF[x][y] != -1 and distF[x][y]<=distJ[xy[0]][xy[1]]+1:
            continue
        distJ[x][y] = distJ[xy[0]][xy[1]] + 1
        queJ.append([x,y])

print("IMPOSSIBLE")
