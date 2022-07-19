#시간초과
#리스트의 insert와 del은 O(n)
#삽입 삭제가 자주 일어남, 다른 자료구조 필요

list_word = []
word = input()
cursor = len(word)

for i in range(cursor):
    list_word.append(word[i])

   
M = int(input())
for i in range(M):
    op = input()
    if op=="L":
        if(cursor!=0):
            cursor-=1
    elif op=="D":
        if(cursor!=len(list_word)):
            cursor+=1
    elif op=="B":
        del list_word[cursor-1]
    else:
        code = input()
        list_word.insert(cursor,code)
        cursor+=1

answer=''

for i in list_word:
    answer+=i
print(answer)
            
