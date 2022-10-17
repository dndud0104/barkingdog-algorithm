#백트래킹, minmax
#https://school.programmers.co.kr/learn/courses/30/lessons/92345
import copy

board = [[1, 1, 1, 1, 1]]
aloc = [0, 0]
bloc = [0, 4]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
row = 0
col = 0

visit = [[0]*5 for _ in range(5)]#문제에 주어진 최대 값이 5*5
block = [[0]*5 for _ in range(5)]

#현재 플레이어의 x,y 다음플레이어의 x,y
def solve(curx, cury, opx, opy):
    
    #현재 밟고 있는 발판이 사라진 경우
    if visit[curx][cury]:
        return 0
    
    ret = 0
    for index in range(4):
        nx = curx + dx[index]
        ny = cury + dy[index]
        #범위를 벗어나는 경우
        if nx < 0 or nx >= row or ny < 0 or ny >= col:
            continue
        #방문 여부, 발판이 남아있는지 여부
        if visit[nx][ny] or block[nx][ny] == 0:
            continue
        visit[curx][cury] = 1

        #val은 플레이어를 다음 방향으로 이동시켰을 때의 턴 수
        #현재 플레이어와 다음 플레이어의 위치를 바꿔
        #재귀함수 호출함으로 플레이어의 순서를 조절
        #다음 플레이어의 x,y 현재 플레이어의 다음 발판 x,y
        val = solve(opx,opy,nx,ny) + 1

        #백트래킹
        visit[curx][cury] = 0

        # 1. 현재 저장된 턴은 패배인데 새로 계산된 턴은 승리인 경우
        if ret % 2 == 0 and val % 2 == 1:
            ret = val # 바로 갱신
        # 2. 현재 저장된 턴과 새로 계산된 턴이 모두 패배인 경우
        elif ret % 2 == 0 and val % 2 == 0:
            ret = max(ret, val) # 최대한 늦게 지는걸 선택
        # 3. 현재 저장된 턴과 새로 계산된 턴이 모두 승리인 경우
        elif ret % 2 == 1 and val % 2 == 1:
            ret = min(ret, val) # 최대한 빨리 이기는걸 선택
            
    return ret


        
        
def solution(board, aloc, bloc):
    global row
    global col
    global block
    row = len(board)
    col = len(board[0])
    block = board.copy()
    
    return solve(aloc[0], aloc[1], bloc[0], bloc[1])
