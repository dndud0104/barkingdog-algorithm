#리스트 사용
from collections import deque

N, K = map(int, input().split())

dx = [-1, 1]
que = deque([])
dist = [-1 for i in range(100001)]

que.append(N)
dist[N] = 0

while dist[K]==-1:
    x = que.popleft()
    for nextX in (x-1, x+1, x*2):
        if nextX < 0 or nextX > 100000:
            continue
        if dist[nextX]!=-1:
            continue
        dist[nextX] = dist[x] + 1
        que.append(nextX)

print(dist[K])
