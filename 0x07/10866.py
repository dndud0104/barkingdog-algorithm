import sys
from collections import deque

N = int(input())
QUE = deque([])

for i in range(N):
    op = sys.stdin.readline().split()

    if op[0]=='push_back':
        QUE.append(op[1])
    if op[0]=='push_front':
        QUE.appendleft(op[1])
    elif op[0]=='pop_front':
        if QUE:
            print(QUE.popleft())
        else:
            print(-1)
    elif op[0]=='pop_back':
        if QUE:
            print(QUE.pop())
        else:
            print(-1)
    elif op[0]=='size':
        print(len(QUE))
    elif op[0]=='empty':
        if QUE:
            print(0)
        else:
            print(1)
    elif op[0]=='front':
        if QUE:
            print(QUE[0])
        else:
            print(-1)
    elif op[0]=='back':
        if QUE:
            print(QUE[-1])
        else:
            print(-1)
