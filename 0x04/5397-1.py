#스택

N = int (input())
for i in range(N):
    L = input()
    cursor = 0
    Left = []
    Right = []
    answer = ''
    for i in L:
        if i =='<':
            if len(Left)>0:
                Right.append(Left.pop())
            else:
                continue
        elif i =='>':
            if len(Right)>0:
                Left.append(Right.pop())
            else:
                continue
        elif i == '-':
            if len(Left)>0:
                Left.pop()
            else:
                continue
        else:
            Left.append(i)
            
    for i in Left:
        answer+=i
    for i in range(len(Right)):
        answer+=Right.pop()
    print(answer)
