#https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3

def solution(sizes):
    answer = 0
    row_size=len(sizes)
    for i in range (row_size):
        if(sizes[i][0]<sizes[i][1]):
            tmp=sizes[i][0]
            sizes[i][0]=sizes[i][1]
            sizes[i][1]=tmp
    
    w=[]
    h=[]
    for i in range (row_size):
        w.append(sizes[i][0])
        h.append(sizes[i][1])
    w.sort()
    h.sort()
    answer=w[-1]*h[-1]
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))
