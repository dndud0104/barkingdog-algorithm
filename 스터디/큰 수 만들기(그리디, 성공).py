#https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = []
    count = 0
    lst_num = list(reversed([int(i) for i in number]))
    index = 0
    
    answer.append(lst_num.pop())
    while lst_num:
        if answer[-1]>=lst_num[-1]:
            answer.append(lst_num.pop())
            continue
        while answer and answer[-1]<lst_num[-1]:
            answer.pop()
            count+=1
            if count==k:
                break
        answer.append(lst_num.pop())
        if count == k:
            break
    
    while lst_num:
        answer.append(lst_num.pop())
    
    while count!=k:
        answer.pop()
        count+=1
    answer = ''.join(map(str,answer))

        

    
    return answer

number = "1924"
k = 2
print(solution(number,k))
