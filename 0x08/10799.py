laser = input()
stack = []
answer = 0
steel = 0
for word in laser:
    if not stack:
        stack.append(word)
        continue
    
    if word == '(':
        if stack[-1] == '(':
            steel += 1
        stack.append(word)
    if word == ')':
        if stack[-1] == ')':
            steel -= 1
            answer += 1
        else:
            answer += steel
        stack.append(word)
        
print(answer)
