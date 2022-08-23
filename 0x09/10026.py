from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(N, RGB):
    visit = [[-1]*N for i in range(N)]
    que = deque([])
    count = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == -1:
                que.append([i,j])
                visit[i][j] = 1
                count += 1
                
            while que:
                xy = que.popleft()
                for index in range(4):
                    nx = xy[0] + dx[index]
                    ny = xy[1] + dy[index]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if visit[nx][ny] != -1 or RGB[nx][ny] != RGB[xy[0]][xy[1]]:
                        continue
                    visit[nx][ny] = 1
                    que.append([nx,ny])
    return count


N = 5
RGB = [['R', 'R', 'R', 'B', 'B'],
       ['G', 'G', 'B', 'B', 'B'],
       ['B', 'B', 'B', 'R', 'R'],
       ['B', 'B', 'R', 'R', 'R'],
       ['R', 'R', 'R', 'R', 'R']]

##N = int(input())
##RGB = []
##for i in range(N):
##    tmp = input()
##    tmp2 = []
##    for j in tmp:
##        tmp2.append(j)
##    RGB.append(tmp2)




#일반인
common = bfs(N, RGB)

#적록색약
for i in range(N):
    for j in range(N):
        if RGB[i][j] == 'G':
            RGB[i][j] = 'R'

rrg = bfs(N, RGB)


print(common, rrg)
