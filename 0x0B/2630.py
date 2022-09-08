def check(N,x,y):
    for r in range(x,x+N):
        for c in range(y,y+N):
            if paper[x][y]!=paper[r][c]:
                return False
    return True

#1. 함수 정의
def P_counter(N, x, y):
#2. base condition
    if check(N,x,y):
        dic[paper[x][y]] += 1
        return
#3. 재귀식
    m = N//2
    for i in range(2):
        for j in range(2):
            P_counter(m, x+i*m, y+j*m)


N = int(input())

paper = []
for _ in range(N):
    paper.append(list(map(int,input().split())))

dic = {0:0, 1:0}

P_counter(N,0,0)

print(dic[0])
print(dic[1])
