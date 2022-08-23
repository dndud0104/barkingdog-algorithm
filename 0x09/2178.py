from collections import deque

n, m = input().split()
n = int(n)
m = int(m)
##n = 4
##m = 6
minLength = 0
mage = []
visit = [[0]*m for i in range(n)]
for row in range(n):
    tmp = input()
    lst = [int(i) for i in tmp]
    mage.append(lst)

##mage = [[1, 1, 0, 1, 1, 0],
##        [1, 1, 0, 1, 1, 0],
##        [1, 1, 1, 1, 1, 1],
##        [1, 1, 1, 1, 0, 1]]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
que = deque([])

visit[0][0] = 1
que.append((1,[0,0]))
while que:
##    print(que)
    length, xy = que.popleft()
    if xy[0] == n-1 and xy[1] == m-1:
        minLength = length
        
##    print(length, xy)
    for index in range(4):
        x = xy[0] + dx[index]
        y = xy[1] + dy[index]
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        if visit[x][y] or mage[x][y] != 1:
            continue
        visit[x][y] = 1
        que.append((length + 1,[x,y]))

print(minLength)
