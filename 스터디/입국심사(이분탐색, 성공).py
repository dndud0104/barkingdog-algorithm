#이분탐색
#https://school.programmers.co.kr/learn/courses/30/lessons/43238
import math

##n = 6
##times = [7,10]

n = 6
times = [6,8,13,17,21]



def solution(n, times):
    answer = 0
    maxTime = max(times) * n
    minTime = 0
    
    while minTime < maxTime:
        mid = (minTime + maxTime)//2
        ableCount = 0 #mid가 주어질때 검사 가능한 사람 수
        for time in times:
            ableCount += mid//time
            if ableCount >= n:
                maxTime = mid
                break 
        if ableCount < n:
            minTime = mid + 1
            #검사 가능한 수가 n보다 작으면 그보다 큰수를 최소값으로 저장
            #mid 값은 n명으로 만들수 없다는것이 확인되었으므로 1을 더하여 최소값으로 저장
            
    answer = minTime
    
    return answer




print(solution(n, times))
