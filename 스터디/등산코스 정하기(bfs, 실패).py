#bfs
#https://school.programmers.co.kr/learn/courses/30/lessons/118669
from collections import deque

##n = 7
##paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
##gates = [3,7]
##summits = [1,5]

n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1,3]
summits = [5]


def solution(n, paths, gates, summits):
    answer = [n,10000000]
    path_dict = {}
    for a in paths:
        if a[0] in path_dict:
            path_dict[a[0]].append([a[1],a[2]])
        else:
            path_dict[a[0]]=[[a[1],a[2]]]
        if a[1] in path_dict:
            path_dict[a[1]].append([a[0],a[2]])
        else:
            path_dict[a[1]]=[[a[0],a[2]]]
    
    que = deque([])
    for start in gates:
        que.append([start,0,[start]])

    while que:
        mid, cost, visit = que.popleft()
        if mid in summits:
            if answer[1]>cost:
                answer = [mid,cost]
            elif answer[1]==cost:
                answer = [min(answer[0],mid),cost]
            continue
        arr = path_dict[mid]
        for next_mid in arr:
            tmp_visit = visit.copy()
            if next_mid[0] in gates:
                continue
            if next_mid[0] in tmp_visit:
                continue
            tmp_visit.append(next_mid[0])
            que.append([next_mid[0], max(cost,next_mid[1]),tmp_visit])
            
        
    return answer


print(solution(n, paths, gates, summits))
