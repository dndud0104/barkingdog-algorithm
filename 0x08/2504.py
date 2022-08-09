PS = input()
stack = []
answer = 0
tmp = 1
for i in range(len(PS)):
    if PS[i]=='(':
        tmp*=2
        stack.append(PS[i])
    elif PS[i]=='[':
        tmp*=3
        stack.append(PS[i])
    elif PS[i]==')':
        if not stack or stack[-1]=='[':
            stack.append(PS[i])
            break
        elif PS[i-1]=='(':
            answer+=tmp
        tmp//=2
        stack.pop()
    else:
        if not stack or stack[-1]=='(':
            stack.append(PS[i])
            break
        elif PS[i-1]=='[':
            answer+=tmp
        tmp//=3
        stack.pop()

if not stack:
    print(answer)
else:
    print(0)

        
