from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]
dz = [1, -1]

def bfs(M,N,H,tomato):
    que = deque([])
    answer = 0
    
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 1:
                    que.append([i,j,k])

    while que:
        xyz = que.popleft()
        for index in range(4):
            x = xyz[1] + dx[index]
            y = xyz[2] + dy[index]
            z = xyz[0]
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            if tomato[z][x][y] == -1 or tomato[z][x][y] != 0:
                continue
            tomato[z][x][y] = tomato[xyz[0]][xyz[1]][xyz[2]] + 1
            que.append([z,x,y])

        for index in range(2):
            x = xyz[1]
            y = xyz[2]
            z = xyz[0] + dz[index]
            if z < 0 or z >= H:
                continue
            if tomato[z][x][y] == -1 or tomato[z][x][y] != 0:
                continue
            tomato[z][x][y] = tomato[xyz[0]][xyz[1]][xyz[2]] + 1
            que.append([z,x,y])

    for i in tomato:
        for j in i:
            for k in j:
                if k==0:
                    return -1
            answer = max(answer, max(j))
  
    return answer-1

M, N, H = input().split()
M = int(M)
N = int(N)
H = int(H)
tomato = []
for i in range(H):
    tmp = []
    for i in range(N):
        tmp.append(list(map(int, input().split())))
    tomato.append(tmp)

##M = 5
##N = 3
##H = 1
##tomato = [[[0, -1, 0, 0, 0],
##           [-1, -1, 0, 1, 1],
##           [0, 0, 0, 1, 1]]]


print(bfs(M,N,H,tomato))     


