def check(N, x, y):
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[x][y]!=paper[i][j]:
                return False
    return True

#1. 함수 정의
def P_counter(N, x, y):
#2. base condition
    if check(N,x,y):
        dic[paper[x][y]] += 1
        return
#3. 재귀식
    m = N//3
    for i in range(3):
        for j in range(3):
            P_counter(m, x+i*m, y+j*m)



N = int(input())

paper = []
for _ in range(N):
    paper.append(list(map(int,input().split())))

##N = 9
##paper = [[0, 0, 0, 1, 1, 1, -1, -1, -1],
##         [0, 0, 0, 1, 1, 1, -1, -1, -1],
##         [0, 0, 0, 1, 1, 1, -1, -1, -1],
##         [1, 1, 1, 0, 0, 0, 0, 0, 0],
##         [1, 1, 1, 0, 0, 0, 0, 0, 0],
##         [1, 1, 1, 0, 0, 0, 0, 0, 0],
##         [0, 1, -1, 0, 1, -1, 0, 1, -1],
##         [0, -1, 1, 0, 1, -1, 0, 1, -1],
##         [0, 1, -1, 1, 0, -1, 0, 1, -1]]

dic = {-1:0, 0:0, 1:0}

P_counter(N,0,0)
print(dic[-1])
print(dic[0])
print(dic[1])



