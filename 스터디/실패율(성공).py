#https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    tmp_list = []
    sort_list = []
    stage_len = len(stages)
    for j in range(N):
        count=0
        for i in range(len(stages)):
            if stages[i]>j+1:
                count+=1
        if count==0 and stage_len==0:
            tmp_list.append([0,j])
            continue
        else:
            tmp_list.append([1-count/stage_len,j])
            stage_len=count
    
    sort_list = sorted(tmp_list, key = lambda x : (-x[0], x[1]))
    for i in range(N):
        answer.append(sort_list[i][1]+1)
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N,stages))
