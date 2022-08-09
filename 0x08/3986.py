count = 0

N = int(input())

for i in range(N):
    stack = []
    pairWord = input()
    for word in pairWord:
        if not stack:
            stack.append(word)
        elif stack[-1] == word:
            stack.pop()
        elif stack[-1] != word:
            stack.append(word)

    if not stack:
        count+=1

print(count)
