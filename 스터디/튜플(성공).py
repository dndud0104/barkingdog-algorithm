#https://school.programmers.co.kr/learn/courses/30/lessons/64065

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"


def solution(s):
    answer = []
    lst_num = []
    lst_tmp = []
    i=0
    tmp=0
    while True:
        if i == len(s):
            break
        if s[i].isdigit():
            tmp=tmp*10+int(s[i])
        elif s[i]=="}":
            if tmp !=0:
                lst_tmp.append(tmp)
            tmp=0
            lst_num.append(lst_tmp)
            lst_tmp = []
        else:
            if tmp !=0:
                lst_tmp.append(tmp)
            tmp=0
        i+=1
        
    lst_num.pop()
    lst_num.sort(key = len)
    
    for num in lst_num:
        for k in num:
            if k not in answer:
                answer.append(k)
    return answer


print(solution(s))
