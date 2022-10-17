#완전탐색
#https://school.programmers.co.kr/learn/courses/30/lessons/42840
import math

def solution(answers):
    supoja = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = []
    result = []
    length = len(answers)

    for i in range(len(supoja)):
        if len(supoja[i])<length:
            supoja[i] = supoja[i]*math.ceil(length/len(supoja[i]))
            
    for j in range(len(supoja)):
        count = 0
        for i in range(len(answers)):
            if supoja[j][i] == answers[i]:
                count+=1
        result.append(count)
        
    max = result[0]
    for i in range(1,3):
        if max < result[i]:
            max = result[i]
    for i in range(3):
        if max == result[i]:
            answer.append(i+1)
            
    
    return answer


answers = [1,3,2,4,2,1,5,3,1,1,2,4,2]
print(solution(answers))
