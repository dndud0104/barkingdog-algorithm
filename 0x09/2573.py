from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def melt(N, M,iceberg):
    que = deque([])
    yearAgo = iceberg.copy()
    visit = [[0]*M for _ in range(N)]

    count = 0
    for i in range(N):
        for j in range(M):
            if iceberg[i][j]!=0 and visit[i][j] == 0:
                que.append((i,j))
                visit[i][j] = 1
                count+=1
                
                while que:
                    x, y = que.popleft()
                    for index in range(4):
                        nx = x + dx[index]
                        ny = y + dy[index]
                        if nx < 0 or nx >= N or ny < 0 or ny >=M:
                            continue
                        if visit[nx][ny] != 0:
                            continue
                        if iceberg[nx][ny] == 0:
                            yearAgo[x][y] -= 1
                            if yearAgo[x][y] < 0:
                                yearAgo[x][y] = 0
                            continue
                        visit[nx][ny] = 1
                        que.append((nx,ny))
    if count == 0:
        return 0,[]
    return count, yearAgo

def bfs():
    N, M = map(int,input().split()) #세로, 가로
    iceberg = []
    for i in range(N):
        tmp = list(map(int, input().split()))
        iceberg.append(tmp)

##    N = 5
##    M = 7
##    iceberg = [[0, 0, 0, 0, 0, 0, 0],
##               [0, 2, 4, 5, 3, 0, 0],
##               [0, 3, 0, 2, 5, 2, 0],
##               [0, 7, 6, 2, 4, 0, 0],
##               [0, 0, 0, 0, 0, 0, 0]]

    i = 0
    while True:
        count, iceberg = melt(N, M,iceberg)
##        print(str(i)+'년차, '+str(count))
##        for a in iceberg:
##            print(a)
        if count >= 2:
            return i
        elif count == 0:
            return 0
        i+=1

    return 0


print(bfs())
