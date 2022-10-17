#다익스트라
#https://school.programmers.co.kr/learn/courses/30/lessons/118669
##n = 6
##paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
##gates = [1,3]
##summits = [5]


n = 7
paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
gates = [3, 7]
summits = [1, 5]


def solution(n, paths, gates, summits):
    def get_smallest_node():
        min_val = int(1e7)
        index = 0
        #해당 노드가 방문한적이 없고 비용이 더 작다면
        for i in range(1,n+1):
            if max(corse[i]) < min_val and not visit[i]:
                min_val = max(corse[i])
                index = i
        #비용이 가장 작은 인덱스를 반환
        return index
    path_dict = {}
    #리스트로 정의된 노드의 정보를 딕셔너리로 저장
    for a in paths:
        if a[0] in path_dict:
            path_dict[a[0]].append([a[1],a[2]])
        else:
            path_dict[a[0]]=[[a[1],a[2]]]
        if a[1] in path_dict:
            path_dict[a[1]].append([a[0],a[2]])
        else:
            path_dict[a[1]]=[[a[0],a[2]]]

    for end in summits:
        del path_dict[end]
    answer = []
    
    for start in gates:
        corse = [[int(1e7)] for _ in range(n+1)]
        visit = [0]*(n+1)
        
        #시작 노드와 연결된 노드의 거리를 저장
        visit[start] = 1
        corse[start] = [0]
        for i in path_dict[start]:
            corse[i[0]] = [i[1]]

        #거리가 구해진 노드중 가장 짧은 거리인 것을 선택
        for _ in range(n-1):
            now = get_smallest_node()
            visit[now] = 1
            #기존 입력된 값보다 더 작은 거리가 나온다면, 값을 갱신
            if now not in path_dict:
                continue
            for j in path_dict[now]:
                if max(corse[now]+[j[1]]) < max(corse[j[0]]):
                    corse[j[0]] = corse[now] + [j[1]]


        for end in summits:
            if not  answer:
                answer = [end,max(corse[end])]
            else:
                if answer[1] > max(corse[end]):
                    answer = [end,max(corse[end])]

         
        
    return answer


print(solution(n, paths, gates, summits))
