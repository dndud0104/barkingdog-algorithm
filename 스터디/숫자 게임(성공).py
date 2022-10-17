#https://school.programmers.co.kr/learn/courses/30/lessons/12987
A = [5,1,3,7]
B = [2,2,6,8]




def solution(A, B):
    answer = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    while B:
        if A[-1]<B[-1]:
            answer+=1
            A.pop()
            B.pop()
        else:
            B.pop()
    return answer





print(solution(A,B))
