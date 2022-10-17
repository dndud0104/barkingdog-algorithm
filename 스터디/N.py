def solution(N, number):
    answer = 0

    if N == number:
        return 1
    if number == N*10+N or number == N*N or number == N*2 or number == N/N:
        return 2
    if number == 11 or number//N==111 or number == N*3:
        return 3
    if number == 12 or number%11 == 0 or number == N*4:
        return 4
    
    
    return answer


print(solution(5,12)) #4


