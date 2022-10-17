#이진탐색
#https://school.programmers.co.kr/learn/courses/30/lessons/64062

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3


def solution(stones, k):
    answer = 0
    right = max(stones)
    left = 1
    while left <= right:
        count = 0
        max_cnt = 0
        mid = (left + right)//2
        for i in range(len(stones)):
            if stones[i] <= mid:
                count += 1
                if count >= k:
                    break
            else:
                count = 0
            
        if count < k:
            left = mid + 1
        else:
            right = mid - 1

    return left





print(solution(stones, k))

##왜 안됨
##def solution(stones, k):
##    answer = 0
##    right = max(stones)
##    left = 1
##    while left <= right:
##        count = 0
##        mid = (left + right)//2
##        print(left, mid, right)
##        for i in range(len(stones)):
##            if stones[i] <= mid:
##                count += 1
##            else:
##                count = 0
##            if count >= k:
##                break
##        if count < k:
##            left = mid + 1
##        else:
##            right = mid - 1
##
##    return mid

#당연히 시간초과
##def solution(stones, k):
##    answer = 0
##    while True:
##        count = 0
##        for i in range(len(stones)):
##            if stones[i] != 0:
##                stones[i] -= 1
##                count = 0
##            elif stones[i] == 0:
##                count += 1
##            if count == k:
##                return answer
##        answer += 1
