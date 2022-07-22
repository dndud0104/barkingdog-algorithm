N = int(input())

h = []
stack = []

for i in range(N):
    h.append(int(input()))

stack.append([0,h.pop()])
answer = 0

while h:
    count = 0
    while stack and stack[-1][1]<h[-1]:
        tmp = stack.pop()
        count+=1+tmp[0]

    answer+=count
    stack.append([count,h.pop()])
##    if not stack:
##        answer+=count
##        stack.append([count,h.pop()])
##        break
##    if stack[-1][1]>h[-1]:
##        answer+=count
##        stack.append([count,h.pop()])

print(answer)
            
