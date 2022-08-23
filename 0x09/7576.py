from collections import deque

m, n = input().split()
m = int(m)
n = int(n)
##m = 5
##n = 5
que = deque([])
dx = [1,0,-1,0]
dy = [0,1,0,-1]
tomato = []
answer = 0
for i in range(n):
    tomato.append(list(map(int, input().split())))
##tomato = [[-1, 1, 0, 0, 0],
##          [0, -1, -1, -1, 0],
##          [0, -1, -1, -1, 0],
##          [0, -1, -1, -1, 0],
##          [0, 0, 0, 0, 0]]

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            que.append([i,j])

while que:
    xy = que.popleft()
    for index in range(4):
        x = xy[0] + dx[index]
        y = xy[1] + dy[index]
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        if tomato[x][y] == -1 or tomato[x][y] != 0:
            continue
        tomato[x][y] = tomato[xy[0]][xy[1]] + 1
        que.append([x,y])
        
for i in tomato:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))

print(answer-1)

