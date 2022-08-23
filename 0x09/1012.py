from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

T = int(input())

for case in range(T):
    count = 0
    field = []
    M, N, K = map(int, input().split())
    field = [[0]*M for i in range(N)]
    for area in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
##    M, N, K = 10, 8, 17
##    field = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
##             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
##             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
##             [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
##             [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
##             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
##             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    que = deque([])
    visit = [[0]*M for i in range(N)]

    for row in range(N):
        for col in range(M):
            if field[row][col] == 1 and visit[row][col] == 0:
                que.append([row, col])
                visit[row][col] = 1
                count += 1
                while que:
                    x, y = que.popleft()
                    for index in range(4):
                        nx = x + dx[index]
                        ny = y + dy[index]
                        if nx < 0 or nx >= N or ny < 0 or ny >= M:
                            continue
                        if field[nx][ny] == 0 or visit[nx][ny] == 1:
                            continue
                        que.append([nx,ny])
                        visit[nx][ny] = 1

    print(count)
