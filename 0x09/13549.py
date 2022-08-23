from collections import deque


def bfs():
    N, K = map(int, input().split())
    ##N = 5
    ##K = 17

    que = deque([])
    dic = {}

    que.append([0, N]) #소요시간, 현재 위치
    dic[N] = 0

    while que:
        time, x = que.popleft()
        if x < 100000 and 2*x not in dic:
            dic[2*x] = time
            que.append([time,2*x])
        for nextX in (x-1,x+1):
            if nextX < 0 or nextX > 100000:
                continue
            if nextX in dic:
                continue
            dic[nextX] = time+1
            que.append([time+1,nextX])
            
                
    return dic[K]


print(bfs())

##x-1을 먼저 해야 성공
##x-1을 마지막으로 하면 실패함, 어째서?
##def bfs():
##    N, K = map(int, input().split())
##    ##N = 5
##    ##K = 17
##
##    que = deque([])
##    dic = {}
##
##    que.append([0, N]) #소요시간, 현재 위치
##    dic[N] = 0
##
##    while K not in dic:
##        time, x = que.popleft()
##        for nextX in (x-1, x+1, x*2):
##            if nextX < 0 or nextX > 100000:
##                continue
##            if nextX in dic:
##                continue
##            if nextX/2 == x:
##                dic[nextX] = time
##                que.append([time,nextX])
##            else:
##                dic[nextX] = time+1
##                que.append([time+1,nextX])
##                
##    return dic[K]
