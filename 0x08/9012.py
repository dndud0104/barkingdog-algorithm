N = int(input())

for i in range(N):
    stack = []
    PS = input()
    for word in PS:
        if word == '(':
            stack.append(word)
        elif word == ')' and not stack:
            stack.append(word)
            break
        elif stack and word == ')' and stack[-1] == '(':
            stack.pop()

    if not stack:
        print('YES')
    else:
        print('NO')
