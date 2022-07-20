#시간초과
#이중 for문
#N은 탑의 수, int형
#lst는 list, int형으로 탑의 높이를 저장
#answer는 list, int형으로 수신하는 탑의 번호를 저장

N = int(input()) #N은 int
lst = []
answer = []

##for i in range(N):
##    lst.append(int(input())) #lst에 int형으로 입력받아 추가

lst = list(map(int, input().rstrip().split()))

for i in range(N-1,-1,-1):
    for j in range(i,-1,-1):
        if lst[i]<lst[j]:
            answer.append(j+1) #answer에 int형으로 수신하는 탑의 번호를 저장
            break
        elif j==0:
            answer.append(0) #answer에 int형으로 수신하는 탑의 번호를 저장

answer=list(reversed(answer))

#int 형으로 출력
##for i in range(len(answer)-1):
##    print(answer[i], end=' ')
##print(answer[-1])

#str로 변환하여 출력
print(" ".join(map(str, answer)))
