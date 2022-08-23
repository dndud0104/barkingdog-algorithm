#왜 안될까

from collections import deque

R, C = map(int, input().split())
##R = 4
##C = 4
dx = [1,0,-1,0]
dy = [0,1,0,-1]
count = 0
mage = []
for i in range(R):
    mage.append(input().split())
dist = [[0]*C for i in range(R)]
##mage = [['#', '#', '#', '#'],
##        ['#', 'J', '.', '#'],
##        ['#', '.', 'F', '#'],
##        ['#', '.', '.', '#']]
que = deque([])

for i in range(len(mage)):
    for j in range(len(mage[i])):
        if mage[i][j] == 'J':
            que.append(('J', [i,j]))
        elif mage[i][j] == 'F':
            que.append(('F', [i,j]))
            dist[i][j] = -1
        elif mage[i][j] == '#':
            dist[i][j] = -1

##print(dist)
##for i in mage:
##        print(i)   
##print(que)
while que:
    target, xy = que.popleft()
    if target == 'J' and mage[xy[0]][xy[1]] == 'F':
        continue
    if xy[0] == 0 or xy[0] == R-1 or xy[1] == 0 or xy[0] == C-1:
        if target == 'J':
            break
    for index in range(4):
        x = xy[0] + dx[index]
        y = xy[1] + dy[index]
        if x < 0 or x >= R or y < 0 or y >= C:
            continue
        if target == 'J':
            if mage[x][y] != '.':
                continue
            mage[x][y] = target
            dist[x][y] = dist[xy[0]][xy[1]] + 1
            que.append((target,[x,y]))
        if target == 'F':
            if mage[x][y] == '#' or mage[x][y] == 'F':
                continue
            mage[x][y] = target
            dist[x][y] = -1
            que.append((target,[x,y]))
##    for i in mage:
##        print(i)
##    print(que)

answer = -1
for i in dist:
    answer = max(answer, max(i))

if answer == -1:
    print("IMPOSSIBLE")
else:
    print(answer + 1)
        
    
