def solution(x):
    answer = 0
    minus = 1
    if x<0:
        minus=-1
        x*=-1
        
    while x!=0:
        answer *= 10
        answer += x%10
        x = int(x/10)
    if answer > 2147483648:
        return 0
    else:
        return answer*minus

x = int(input())
print(solution(x))
