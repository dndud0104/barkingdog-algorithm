#딕셔너리 사용
from collections import deque

N, K = map(int, input().split())

que = deque([])
dic = {}

que.append([0, N])
dic[N] = 0

while K not in dic:
    time, x = que.popleft()
    for nextX in (x-1, x+1, x*2):
        if nextX < 0 or nextX > 100000:
            continue
        if nextX in dic:
            continue
        dic[nextX] = time+1
        que.append([time+1,nextX])

print(dic[K])
