#https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    
    student = {i:1 for i in range(1,n+1)}
    for i in range(len(lost)):
        student[lost[i]]-=1
    for i in range(len(reserve)):
        student[reserve[i]]+=1
    
    #1번 판단
    if student[1]==0:
        if student[2]==2:
            student[1]=1
            student[2]=1
            answer+=1
    elif student[1]==1:
        answer+=1
    else:
        if student[2]==0:
            student[1]=1
            student[2]=1
            answer+=1
        else:
            answer+=1
            
    #2~n-1번 판단
    for i in range(2,n):
        if student[i]==0:
            if student[i+1]==2:
                student[i]=1
                student[i+1]=1
                answer+=1 
        elif student[i]==1:
            answer+=1
        else:
            if student[i+1]==0:
                student[i]=1
                student[i+1]=1
                answer+=1
            else:
                answer+=1
    
    #n번 판단           
    if student[n]>=1:
        answer+=1

    return answer

n =5
lost =[2, 4]
reserve=[1, 3, 5]
print(solution(n,lost,reserve))
