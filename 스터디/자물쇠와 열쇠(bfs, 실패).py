#실패, 시간 초과
from collections import deque

key = [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]
lock = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]



def rotate(key):#90도씩 회전
    M = len(key)
    new_key=[[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_key[j][M-1-i] = key[i][j]  
    return new_key

def move(key, direction):
    M = len(key)
    new_key=[[0]*M for _ in range(M)]
    if direction == 0:#상
        for i in range(1,M):
            for j in range(M):
                new_key[i-1][j] = key[i][j]
    elif direction == 1:#하
        for i in range(M-1):
            for j in range(M):
                new_key[i+1][j] = key[i][j]
    elif direction == 2:#좌
        for i in range(M):
            for j in range(1,M):
                new_key[i][j-1] = key[i][j]
    else:#우
        for i in range(M):
            for j in range(M-1):
                new_key[i][j+1] = key[i][j]
           
    return new_key

def extend(key, L):
    new_key=[[0]*L for _ in range(L)]
    M = len(key)
    for i in range(M):
        for j in range(M):
            new_key[i][j] = key[i][j]
    return new_key

def solution(key, lock):
    answer = True
    que = deque([])

    if len(key) != len(lock):
        key = extend(key, len(lock))

        
    que.append(key)
    while que:
        key = que.popleft()
        result = 0
        for a in key:
            result += sum(a)
        if result == 0:
            continue
        for r in range(4):
            loop = True
            key = rotate(key)
            for i in range(len(lock)):
                for j in range(len(lock)):
                    if not key[i][j] ^ lock[i][j]:
                        loop = False
                        break
                if not loop:
                    break
            if loop:
                return True
            
            for m in range(4):
                que.append(move(key,m))

    return False


print(solution(key, lock))
