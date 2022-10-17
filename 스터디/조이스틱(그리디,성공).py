#그리디
#https://school.programmers.co.kr/learn/courses/30/lessons/42860
name = "JEROEN"



def solution(name):
    answer = 0
    
    for a in name:
        if a == chr(65):
            continue
        elif ord(a) <= 78:
            answer+=ord(a)-65
        else:
            answer+=91-ord(a)

    min_tmp = len(name)-1

    for i in range(len(name)-1):
        next_i = i+1

        while next_i<len(name) and name[next_i]=='A':
            next_i+=1
        #이전 최소값, ->+<->,<->+<-
        min_tmp = min(min_tmp,i+2*(len(name)-next_i),2*i+(len(name)-next_i))
        
    
    return answer+min_tmp



print(solution(name))
