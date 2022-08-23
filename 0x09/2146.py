from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]



def division_land(N, land):
    global d_land
    d_land = [[0]*N for _ in range(N)]
    land_num = 0
    que = deque()
    
    for i in range(N):
        for j in range(N):
            if d_land[i][j]==0 and land[i][j] == 1:
                land_num+=1
                d_land[i][j] = land_num
                que.append((i,j))
                
            while que:
                x, y = que.popleft()
                for index in range(4):
                    nx = x + dx[index]
                    ny = y + dy[index]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if d_land[nx][ny] != 0 or land[nx][ny] == 0:
                        continue
                    d_land[nx][ny] = land_num
                    que.append((nx,ny))


def bfs():
    N = int(input())
    land = []
    for _ in range(N):
        tmp = list(map(int,input().split()))
        land.append(tmp)

##    N = 10
##    land = [[1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
##            [1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
##            [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
##            [0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
##            [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
##            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
##            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
##            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
##            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
##            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    
    division_land(N, land) #땅 구분
    

    dist = [[-1]*N for _ in range(N)]
    answer = 2*N
    que = deque()
    for i in range(N):
        for j in range(N):
            if d_land[i][j] != 0:
                dist[i][j] = 0
                que.append((i,j))
            stop = False
            #다리가 이어지면 while문을 멈추기 위함
            while que and not stop:
                x, y = que.popleft()
                for index in range(4):
                    nx = x + dx[index]
                    ny = y + dy[index]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if dist[nx][ny] >= 0 or d_land[nx][ny] == d_land[i][j]:
                        #dist가 0보다 크면 지나간 자리
                        #처음 땅의 번호와 다음 땅의 번호가 같으면 continue
                        continue
                    if d_land[nx][ny] != 0 and d_land[nx][ny] != d_land[i][j]:
                        #다음 땅이 바다가 아니고
                        #처음 땅의 번호와 다음 땅의 번호가 다르면 다리가 이어짐
                        answer = min(answer, dist[x][y]) #가장 짧은 다리를 찾기 위함
                        que.clear()#큐를 비워야 올바른 답을 출력
                        stop = True
                        break
                    #땅에서 벗어나 바다에 다리를 만들고있음
                    dist[nx][ny] = dist[x][y] + 1
                    que.append((nx,ny))
                               
                    
            dist = [[-1]*N for _ in range(N)]
    
    return answer


print(bfs())
