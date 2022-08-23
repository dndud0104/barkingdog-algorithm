from collections import deque


dx1 = [1,0,-1,0]
dy1 = [0,1,0,-1]
dx2 = [-2, -1, 1, 2, 2, 1, -1, -2]
dy2 = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    K = int(input()) #말처럼 동작 가능 수
    W, H = map(int,input().split()) #가로, 세로

    field = []
    for _ in range(H):
        field.append(list(map(int,input().split())))

##    K = 1
##    W, H = 4, 4
##    field = [[0, 0, 0, 0],
##             [1, 0, 0, 0],
##             [0, 0, 1, 0],
##             [0, 1, 0, 0]]

    que = deque([])
    visit = [[[-1]*W for _ in range(H)] for _ in range(K+1)]

    que.append((0,0,0))
    visit[0][0][0] = 0

    while que:
        horse, x, y = que.popleft()
        if x == H - 1 and y == W - 1:
            return visit[horse][x][y]
        #horse가 K번 이하인 경우
        if horse < K:
            for index in range(8):
                nx = x + dx2[index]
                ny = y + dy2[index]
                if nx < 0 or nx >= H or ny < 0 or ny >= W:
                    continue
                if field[nx][ny] == 1 or visit[horse + 1][nx][ny] != -1:
                    continue
                que.append((horse+1,nx,ny))
                visit[horse + 1][nx][ny] = visit[horse][x][y] + 1
        for index in range(4):
            nx = x + dx1[index]
            ny = y + dy1[index]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if field[nx][ny] == 1 or visit[horse][nx][ny] != -1:
                continue
            que.append((horse,nx,ny))
            visit[horse][nx][ny] = visit[horse][x][y] + 1

        
    return -1

print(bfs())
