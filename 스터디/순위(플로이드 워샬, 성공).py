#플로이드 워샬, 그래프
#https://westmino.tistory.com/20
#https://school.programmers.co.kr/learn/courses/30/lessons/49191

from collections import defaultdict

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]] #2
##n = 5
##results = [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]] #1


#알고리즘 풀이
def solution(n, results):
    answer = 0
    board = [[0]*n for _ in range(n)]
    
    for a,b in results:
        board[a-1][b-1] = 1
        board[b-1][a-1] = -1

    
    
    for k in range(n):#k는 거쳐가는 노드
        for i in range(n):#i는 출발 노드
            for j in range(n):#j는 도착 노드
                if i == j or board[i][j] in [1,-1]:#이미 채워진 영역은 건너뛰뜀
                    continue
                if board[i][k] == board[k][j] == 1:
                    board[i][j] = 1
                    board[j][i] = board[k][i] = board[j][k] = -1
                    print(k, i, j)
                    for a in board:
                        print(a)
                    print('-----------------')
                
    for row in board:
        if row.count(0) == 1:
            answer += 1
    return answer

#재현이 풀이
##def solution(n, results):
##    winLog=[[] for i in range(n)]
##    loseLog=[[] for i in range(n)]
##    for result in results:
##        winner,loser=result
##        winLog[winner-1].append(loser-1)
##        loseLog[loser-1].append(winner-1)
##
##    for i in range(n):
##        if len(winLog[i])>0 and len(loseLog[i])>0:
##            for w in winLog[i]:
##                for l in loseLog[i]: #w=4 l=3
##                    if not w in winLog[l]:
##                        winLog[l].append(w)
##                    if not l in loseLog[w]:
##                        loseLog[w].append(l)
##    answer=0
##    print(winLog)
##    print(loseLog)
##    for i in range(n):
##        if len(winLog[i])+len(loseLog[i])==n-1:
##            #print(i)
##            answer+=1
##    return answer




print(solution(n, results))






