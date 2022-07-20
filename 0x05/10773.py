K = int(input())
stack = []

for i in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    elif num != 0:
        stack.append(num)
        
answer = 0
for i in stack:
    answer+=i

print(answer)
