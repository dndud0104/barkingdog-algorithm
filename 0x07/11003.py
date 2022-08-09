import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
A = list(sys.stdin.readline().split())
D = []

print(A[0:])

for i in range(N):
    if i - L + 1 <= 0:
        D.append(min(A[0:i+1]))
    else:
        D.append(min(A[i - L + 1:i+1]))

print(" ".join(D))
