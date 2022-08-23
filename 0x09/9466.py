from collections import deque

def bfs():
    stn = [-1]
    n = int(input())
    tmp = list(map(int,input().split()))
    stn += tmp
##    n = 7
##    stn = [-1,2,3,4,5,6,7,4]
    

    que = deque([])
    solo = 0
    visit = [0]*(n+1)

    for index in range(1,n+1):
        if visit[stn[index]] != -1:
            visit[index]=index
            que.append(stn[index])
        

        while que:
            nt = que.popleft()
            if visit[nt] == 0:
                visit[nt] = index
                que.append(stn[nt])
            elif visit[nt] == -1:
                break
            elif visit[nt] == index:
                while visit[nt] != -1:
                    visit[nt] = -1
                    nt = stn[nt]
            else:
                break

    for index in range(1,n+1):
        if visit[index]!=-1:
            solo+=1
        
    
    return solo

T = int(input())
##T = 1

for i in range(T):
    print(bfs())
