#3차원으로 벽을 부수지 않고 도달하는 경로와
#벽을 1번 부수고 도달하는 경로 2가지로 표현?
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]



def bfs(N,M):
    mage = []
    for i in range(N):
        tmp = input()
        mage.append([int(a) for a in tmp])
##    mage = [[0, 1, 0, 0],
##            [1, 1, 1, 0],
##            [1, 0, 0, 0],
##            [0, 0, 0, 0],
##            [0, 1, 1, 1],
##            [0, 0, 0, 0]]

    que = deque([])
    visit = [[[-1]*M for i in range(N)] for j in range(2)]


    que.append([0,0,0])#벽뚫, 세로, 가로
    visit[0][0][0] = 1
    visit[1][0][0] = 1

    while que:
##        print(que)
##        for a in visit:
##            for b in a:
##                print(b)
##            print('-')
        zxy = que.popleft()
        if zxy[1] == N-1 and zxy[2] == M-1:
            return visit[zxy[0]][zxy[1]][zxy[2]]
        for index in range(4):
            nx = zxy[1] + dx[index]
            ny = zxy[2] + dy[index]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if zxy[0] == 0 and mage[nx][ny] == 1 and visit[zxy[0]][nx][ny] == -1:
                visit[1][nx][ny] = visit[0][zxy[1]][zxy[2]] + 1
                que.append([1,nx,ny])
            elif mage[nx][ny] == 0 and visit[zxy[0]][nx][ny] == -1:
                visit[zxy[0]][nx][ny] = visit[zxy[0]][zxy[1]][zxy[2]] + 1
                que.append([zxy[0],nx,ny])
    
        
    return -1




N, M = map(int,input().split()) #세로, 가로
##N = 6
##M = 4

print(bfs(N,M))
