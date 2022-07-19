#시간초과는 나지 않지만 오래걸림

result = []
N, k = map(int, input().split())

people = [i+1 for i in range(N)]
tmp = []
count = 1
while True:
    people.reverse()
    N = len(people)
    for i in range(N):
        tmp.append(people.pop())
        
        if count%k==0:
            result.append(tmp.pop())
        count+=1
    people = tmp.copy()
    tmp = []
    if not people:
        break

answer='<'
for i in result:
    answer+=str(i)+', '
answer = answer[:-2]+'>'
print(answer)
