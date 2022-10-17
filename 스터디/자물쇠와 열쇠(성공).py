key = [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0]]
lock = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

def find(lock):#lock에서 열쇠와 비교할 영역을 추출
    M = len(lock)
    start = [M-1,M-1]
    end = [0,0]
    for i in range(M):
        for j in range(M):
            if lock[i][j] == 0:
                start = min([i,j],start)
                end = max([i,j],end)

    if start == [M-1,M-1] and end == [0,0]:#처음값과 동일하면 0인 부분이 없는것
        return False
    
    new_lock = []
    for i in range(start[0],end[0]+1):
        tmp = []
        for j in range(start[1],end[1]+1):
            tmp.append(lock[i][j])
        new_lock.append(tmp)

    return new_lock


def rotate(key):#90도씩 회전
    M = len(key)
    new_key=[[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_key[j][M-1-i] = key[i][j]  
    return new_key


def check(key, lock, x, y):#열쇠와 비어있는 부분을 xor
    loop = True
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if not key[x+i][y+j] ^ lock[i][j]:
                loop = False
                break
        if not loop:
            return False
            
    return True

def solution(key, lock):
    lock = find(lock)
    if not lock:
        return True
    K = len(key)
    for r in range(4):
        if K < len(lock) or K < len(lock[0]):
            return False
        for i in range((K-len(lock))+1):
            for j in range((K-len(lock[0]))+1):
                if check(key,lock,i,j):
                    return True
        key = rotate(key)

    return False

print(solution(key, lock))
