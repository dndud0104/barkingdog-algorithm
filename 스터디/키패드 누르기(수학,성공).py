#https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    L = [1,4,7]
    R = [3,6,9]
    lhand=10
    rhand=12
    
    
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i]=11
        if numbers[i] in L:
            answer+="L"
            lhand=numbers[i]
        elif numbers[i] in R:
            answer+="R"
            rhand=numbers[i]
        else:
            tmp_abs=[abs(numbers[i]-lhand),abs(numbers[i]-rhand)]
            dist = [tmp_abs[0]%3+tmp_abs[0]//3,tmp_abs[1]%3+tmp_abs[1]//3]
            if dist[0]<dist[1]:
                answer+="L"
                lhand=numbers[i]
            elif dist[0]>dist[1]:
                answer+="R"
                rhand=numbers[i]
            else:
                if hand=="left":
                    answer+="L"
                    lhand=numbers[i]
                else:
                    answer+="R"
                    rhand=numbers[i]
                

    return answer

numbers =[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand ="right"
print(solution(numbers, hand))
