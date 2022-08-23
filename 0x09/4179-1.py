#얘도 왜 안될까
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
dist = [[-1]*C for i in range(R)]
##mage = [['#','#','#','#'],
##        ['#','J','F','#'],
##        ['#','.','.','#'],
##        ['#','.','.','#']]

que = deque([])

for i in range(len(mage)):
    for j in range(len(mage[i])):
        if mage[i][j] == 'F':
            que.append([i,j])
            dist[i][j] = 0
        elif mage[i][j] == 'J':
            J = [i,j]

print(que)
print(dist)
print(J)

while que:
    print(dist)
    xy = que.popleft()
    for index in range(4):
        x = xy[0] + dx[index]
        y = xy[1] + dy[index]
        if x < 0 or x >= R or y < 0 or y >= C:
            continue
        if mage[x][y] == '#' or dist[x][y] >= 0:
            continue
        dist[x][y] = dist[xy[0]][xy[1]] + 1
        que.append([x,y])
        
que.append(J)
dist[J[0]][J[1]] = 0
        
while que:
    xy = que.popleft()
    for index in range(4):
        x = xy[0] + dx[index]
        y = xy[1] + dy[index]
        if x < 0 or x >= R or y < 0 or y >= C:
            print(dist[xy[0]][xy[1]] + 1)
            exit(0)
        if mage[x][y] == '#' or dist[xy[0]][xy[1]]+1 >= dist[x][y]:
            continue
        dist[x][y] = dist[xy[0]][xy[1]] + 1
        que.append([x,y])

print("IMPOSSIBLE")
