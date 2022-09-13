def check(N,x,y):
    for r in range(x,x+N):
        for c in range(y,y+N):
            if img[x][y]!=img[r][c]:
                return False
    return True

#1. 함수 정의
def QuadTree(N, x, y):
    
#2. base condition
    if check(N,x,y):
        answer.append(str(img[x][y]))
        return
#3. 재귀식
    m = N//2
    answer.append('(')
    for i in range(2):
        for j in range(2):
            QuadTree(m, x+i*m, y+j*m)
    answer.append(')')


N = int(input())

img = []
for _ in range(N):
    tmp = list(map(int,input()))
    img.append(tmp)

##N = 8
##img = [[1, 1, 1, 1, 0, 0, 0, 0],
##       [1, 1, 1, 1, 0, 0, 0, 0],
##       [0, 0, 0, 1, 1, 1, 0, 0],
##       [0, 0, 0, 1, 1, 1, 0, 0],
##       [1, 1, 1, 1, 0, 0, 0, 0],
##       [1, 1, 1, 1, 0, 0, 0, 0],
##       [1, 1, 1, 1, 0, 0, 1, 1],
##       [1, 1, 1, 1, 0, 0, 1, 1]]

answer = []
QuadTree(N,0,0)

print(''.join(answer))
