from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    I = int(input()) #한변의 길이
    S = list(map(int,input().split())) #시작점
    E = list(map(int,input().split())) #종료점
##    I = 8
##    S = [0, 0]
##    E = [7, 0]
    
    board = [[-1]*I for i in range(I)]
    que = deque([])

    board[S[0]][S[1]] = 0
    que.append(S)

    while que:
        xy = que.popleft()
        if xy[0] == E[0] and xy[1] == E[1]:
            return board[xy[0]][xy[1]]
        for index in range(8):
            nx = xy[0] + dx[index]
            ny = xy[1] + dy[index]
            if nx < 0 or nx >= I or ny < 0 or ny >= I:
                continue
            if board[nx][ny] != -1:
                continue
            board[nx][ny] = board[xy[0]][xy[1]] + 1
            que.append([nx,ny])
    return 0

T = int(input()) #테스트 케이스 수
##T = 3
for i in range(T):
    print(bfs())
