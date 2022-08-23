#실패, 2차원으로는 풀리지 않는 문제?
#벽을 부순 이후에는 벽을 부수지 않은 경로를 무시하기 때문?
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
    visit = [[-1]*M for i in range(N)]


    que.append((0,[0,0]))
    visit[0][0] = 1

    while que:
##        for a in visit:
##            print(a)
        hammer, xy = que.popleft()
        if xy[0] == N-1 and xy[1] == M-1:
            return visit[xy[0]][xy[1]]
        for index in range(4):
            nx = xy[0] + dx[index]
            ny = xy[1] + dy[index]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if hammer == 0 and mage[nx][ny] == 1:
                visit[nx][ny] = visit[xy[0]][xy[1]] + 1
                que.append((1,[nx,ny]))
                continue
            if mage[nx][ny] == 1 or visit[nx][ny] != -1:
                continue
            visit[nx][ny] = visit[xy[0]][xy[1]] + 1
            que.append((hammer,[nx,ny]))
    
        
    return -1




N, M = map(int,input().split()) #세로, 가로
##N = 6
##M = 4

print(bfs(N,M))
