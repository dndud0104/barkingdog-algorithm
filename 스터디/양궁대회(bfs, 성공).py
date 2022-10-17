#bfs
#https://school.programmers.co.kr/learn/courses/30/lessons/92342

from collections import deque

def solution(n, info):

    answer = [] #차가 가장큰 배열을 담는 배열
    q = deque([(0,[0,0,0,0,0,0,0,0,0,0,0])]) #현재 과녁 인덱스와 라이언이 쏴야할 배열
    maxsub = 0 #라이언과 어피치의 최대 점수차를 저장

    while q:
        index, lionarr = q.popleft() #데크에서 왼쪽의 값을 pop
        if sum(lionarr) == n: #라이언이 화살을 다 쏜경우
            apeach = 0
            lion = 0
            for i in range(11):
                if not (info[i] == 0 and lionarr[i] == 0):#두명이 0점이 아니고
                    if info[i] >= lionarr[i]: #어피치가 점수가 높은 경우
                        apeach += 10 - i
                    else: #라이언이 점수가 높은 경우
                        lion += 10 - i
            if lion > apeach: #라이언의 점수가 더 크면
                sub = lion - apeach
                if maxsub <= sub:#이전 최대 점수차보다 크거나 같으면
                    maxsub = sub#최대 점수차 갱신
                    answer.clear()
                    answer.append(lionarr)#새로운 결과를 저장
                else:
                    continue
        elif sum(lionarr) > n:#화살을 더 많이 쏜 경우
            continue
        elif index == 10: #과녁의 마지막에 도달했으나 화살이 남은 경우
            tmp = lionarr.copy()
            tmp[index] = n - sum(tmp) #마지막 점수에 남은 화살을 몰아줌
            q.append((-1,tmp))
        else:#과녁의 마지막이 아니고 index != 10, 화살이 남아있는 경우
            tmp = lionarr.copy()
            tmp[index] = info[index] + 1
            q.append((index + 1, tmp))#어피치보다 많이 쏴서 높은 점수를 얻는 경우
            tmp2 = lionarr.copy()
            tmp2[index] = 0
            q.append((index + 1, tmp2))#어피치에게 점수를 주고 넘어가는 경우

    if not answer:
        return [-1]
    else:
        return answer[0]

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]

print(solution(n,info))
