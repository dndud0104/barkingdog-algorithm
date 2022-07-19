#시간초과
#리스트의 insert와 del은 O(n)
#삽입 삭제가 자주 일어남, 다른 자료구조 필요

N = int (input())
for i in range(N):
    L = input()
    cursor = 0
    L_answer = []
    answer = ''
    for i in L:
        if i =='<':
            if cursor == 0:
                continue
            else:
                cursor-=1
        elif i =='>':
            if cursor < len(L_answer):
                cursor+=1
            else:
                continue
        elif i == '-':
            if cursor == 0:
                continue
            else:
                del L_answer[cursor-1]
                cursor-=1
        else:
            L_answer.insert(cursor, i)
            cursor+=1
    for i in L_answer:
        answer+=i
    print(answer)
