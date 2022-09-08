#1. 함수 정의
def P_counter(N, sx, sy, ex, ey):
    start = paper[sx][sy]
    loop = True
    for x in range(sx, ex):
        for y in range(sy, ey):
            if start != paper[x][y]:
                P_counter(N//3,sx, sy, sx+N//3, sy+N//3)
                P_counter(N//3,sx, sy+N//3, sx+N//3, sy+N//3*2)
                P_counter(N//3,sx, sy+N//3*2, sx+N//3, sy+N)
                P_counter(N//3,sx+N//3, sy, sx+N//3*2, sy+N//3)
                P_counter(N//3,sx+N//3, sy+N//3, sx+N//3*2, sy+N//3*2)
                P_counter(N//3,sx+N//3, sy+N//3*2, sx+N//3*2, sy+N)
                P_counter(N//3,sx+N//3*2, sy, sx+N, sy+N//3)
                P_counter(N//3,sx+N//3*2, sy+N//3, sx+N, sy+N//3*2)
                P_counter(N//3,sx+N//3*2, sy+N//3*2, sx+N, sy+N)
                loop = False
                break
        if not loop:
            break
    if loop:
        dic[start] = dic[start] + 1
##        print(sx, sy, ex, ey)



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
sx, sy = 0 , 0
ex, ey = N, N

P_counter(N, sx, sy, ex, ey)
print(dic[-1])
print(dic[0])
print(dic[1])



