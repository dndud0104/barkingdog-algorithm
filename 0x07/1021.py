from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

que = deque([i for i in range(1,int(N)+1)])
count = 0

for a in num:
    if que[0] == a:
        que.popleft()
        continue
    tmpQ = que.copy()
    tmpC = 0
    while tmpQ[0] != a:
        tmpQ.append(tmpQ.popleft())
        tmpC+=1
    if tmpC <= len(que)/2:
        count += tmpC
        que = tmpQ
        que.popleft()
        continue
    tmpQ = que.copy()
    tmpC = 0
    while tmpQ[0] != a:
        tmpQ.appendleft(tmpQ.pop())
        tmpC+=1
    count += tmpC
    que = tmpQ
    que.popleft()
        
print(count)
