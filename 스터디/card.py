#틀림 문제 해결을 못하겠음
board = [[0, 0, 1, 0], [1, 0, 0, 0], [4, 4, 3, 2], [0, 3, 2, 0]]
#board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 2
c = 0




def solution(board, r, c):
    enter = 0
    direction = 0
    count = 0
    
    for i in range(4):
        for j in range(4):
            if board[i][j]!=0:
                count += 1
    
    while enter != count:
        if board[r][c]==0:
            move = False
            minMove = 3
            for row in range(4):
                for col in range(4):
                    tmp = 0
                    if board[row][col] != 0:
                        if r != row:
                            tmp+=1
                        if c != col:
                            tmp+=1
                        if minMove > tmp:
                            minMove = tmp
                            tmpR = row
                            tmpC = col
                            tmpD = tmp
            
            r = tmpR
            c = tmpC
            direction += tmpD
        print(r,c,board[r][c])
        if board[r][c]!=0:
            num = board[r][c]
            enter += 1
            board[r][c] = 0
            pair = False

        
        
        for row in range(4):
            if num in board[row]:
                if row != r:
                    r = row
                    direction += 1
                for col in range(4):
                    if num == board[row][col]:
                        if col != c:
                            c = col
                            direction += 1
                        board[r][c] = 0
                        enter += 1
                        pair = True
                        break    
                    
            if pair:
                break
        print(r,c,board[r][c])
        
        print(enter, direction)

    return enter + direction




print(solution(board, r, c))
