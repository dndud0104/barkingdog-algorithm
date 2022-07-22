N = int(input())
A = list(map(int, input().rstrip().split()))

A = list(reversed(A))
index = 0
stack = []
answer=[-1]*N

stack.append([index, A.pop()])

while A:
    index+=1
    while stack and stack[-1][1]<A[-1]:
        tmp = stack.pop()
        answer[tmp[0]]=A[-1]
    stack.append([index, A.pop()])

print(" ".join(map(str,answer)))
