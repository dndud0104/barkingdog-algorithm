#스택

N = int(input()) 
lst = []
answer = []
stack = []
i = 0

lst = list(map(int, input().rstrip().split()))
lst=list(reversed(lst))

answer.append(0)
stack.append([i,lst.pop()])

while True:
    i+=1
    if not lst:
        break
    while stack and stack[-1][1]<lst[-1]:
        stack.pop()
    if not stack:
        answer.append(0)
        stack.append([i,lst.pop()])
        continue
    if stack[-1][1]>lst[-1]:
        answer.append(stack[-1][0]+1)
        stack.append([i,lst.pop()])
        

print(" ".join(map(str, answer)))
