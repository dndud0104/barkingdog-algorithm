from collections import deque


def card(N):
    count = 1
    que = deque([i for i in range(1,N+1)])

    while len(que)!=1:
        que.popleft()
        if len(que)==1:
            break
        que.append(que.popleft())
    return que.pop()
    

N = int(input())
print(card(N))
