#https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    L = [1,4,7]
    R = [3,6,9]
    M = [2,5,8,0]
    lpoint=3
    rpoint=3
    lhand='L'
    rhand='R'    
    
    for i in range(len(numbers)):
        if numbers[i] in L:
            answer+="L"
            lpoint=L.index(numbers[i])
            if lhand=="M":
                lhand="L"
        elif numbers[i] in R:
            answer+="R"
            rpoint=R.index(numbers[i])
            if rhand=="M":
                rhand="R"
        else:
            mpoint=M.index(numbers[i])
            if rhand=="M":
                if abs(lpoint-mpoint)>abs(rpoint-mpoint)-1:
                    answer+="R"
                    rpoint=mpoint
                    rhand="M"
                elif abs(lpoint-mpoint)<abs(rpoint-mpoint)-1:
                    answer+="L"
                    lpoint=mpoint
                    lhand="M"
                else:
                    if hand=="right":
                        answer+="R"
                        rpoint=mpoint
                        rhand="M"
                    else:
                        answer+="L"
                        lpoint=mpoint
                        lhand="M"
            elif lhand=="M":
                if abs(lpoint-mpoint)-1>abs(rpoint-mpoint):
                    answer+="R"
                    rpoint=mpoint
                    rhand="M"
                elif abs(lpoint-mpoint)-1<abs(rpoint-mpoint):
                    answer+="L"
                    lpoint=mpoint
                    lhand="M"
                else:
                    if hand=="right":
                        answer+="R"
                        rpoint=mpoint
                        rhand="M"
                    else:
                        answer+="L"
                        lpoint=mpoint
                        lhand="M"
            else:
                if abs(lpoint-mpoint)>abs(rpoint-mpoint):
                    answer+="R"
                    rpoint=mpoint
                    rhand="M"
                elif abs(lpoint-mpoint)<abs(rpoint-mpoint):
                    answer+="L"
                    lpoint=mpoint
                    lhand="M"
                else:
                    if hand=="right":
                        answer+="R"
                        rpoint=mpoint
                        rhand="M"
                    else:
                        answer+="L"
                        lpoint=mpoint
                        lhand="M"

    return answer

numbers =[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand ="right"
print(solution(numbers, hand))
