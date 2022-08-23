from collections import deque

##n, m = input().split()
##n = int(n)
##m = int(m)
n = 4
m = 6
mage = []
length = [[-1]*m for i in range(n)]
##for row in range(n):
##    tmp = input()
##    lst = [int(i) for i in tmp]
##    mage.append(lst)

mage = [[1, 1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1]]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
que = deque([])

length[0][0] = 0
que.append([0,0])
while que:
##    print(que)
    xy = que.popleft()
        
##    print(length, xy)
    for index in range(4):
        x = xy[0] + dx[index]
        y = xy[1] + dy[index]
        if x < 0 or x >= n or y < 0 or y >= m:
            continue
        if length[x][y] >=0 or mage[x][y] != 1:
            continue
        length[x][y] = length[xy[0]][xy[1]] + 1
        que.append([x,y])

print(length[n-1][m-1]+1)
