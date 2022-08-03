#deque를 써도 시간초과
#input() 대신 sys.stdin.readline()를 사용해야함
import sys

N = int(input())
QUE = []
for i in range(N):
    op = sys.stdin.readline().split()

    if op[0]=='push':
        QUE.append(op[1])
    elif op[0]=='pop':
        if QUE:
            print(QUE.pop(0))
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
