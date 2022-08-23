from collections import deque

n, m = input().split()
n = int(n)
m = int(m)
##n = 6
##m = 5

paper = []
visit = [[0]*m for i in range(n)]
que = deque([])
dx = [1,0,-1,0]
dy = [0,1,0,-1]
count = 0
maxArea = 0

for i in range(n):
    paper.append(list(map(int,input().split())))
##paper = [[1, 1, 0, 1, 1],
##         [0, 1, 1, 0, 0],
##         [0, 0, 0, 0, 0],
##         [1, 0, 1, 1, 1],
##         [0, 0, 1, 1, 1],
##         [0, 0, 1, 1, 1]]
###사전작업###

for row in range(n):
    for col in range(m):
        if visit[row][col] or paper[row][col] != 1:
            continue
        #1. 시작칸을 큐에 넣고 방문했다는 표시를 남김
        count += 1
        visit[row][col] = 1
        que.append([row,col])
        #2. 큐에서 원소를 꺼내어 그 칸에 상하좌우로 인접한 칸에 대해 3번을 진행
        area = 1
        while que:
            xy = que.popleft()
            for index in range(4):
                x = xy[0] + dx[index]
                y = xy[1] + dy[index]
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
        #3. 해당 칸을 이전에 방문했다면 아무것도 하지 않고,
                if visit[x][y] or paper[x][y] != 1:
                    continue
        #처음으로 방문했다면 방문했다는 표시를 남기고 해당 칸을 큐에 삽입
                visit[x][y] = 1
                que.append([x,y])
                area += 1
        #4. 큐가 빌 때까지 2번을 반복
        if area > maxArea:
            maxArea = area
        
print(count)
print(maxArea)





