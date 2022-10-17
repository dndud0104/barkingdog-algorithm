#https://school.programmers.co.kr/learn/courses/30/lessons/42861
##n = 4
##costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 6
costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
def solution(n, costs):
    answer = 0
    count = 0
    index = 0
    tmp = []
    maxleng = len(costs)
    island = [0 for i in range(n)]
    costs.sort(key = lambda x : x[2])
    print(costs)
    #이미 최소개수
    if len(costs)==n-1:
        for k in costs:
            answer+=k[2]
        return answer
    print(island)
    island[costs[0][0]]=1
    island[costs[0][1]]=1
    answer+=costs[0][2]
    index+=1
    count+=1
    #아닌경우
    while count!=(n-1):
        if index == (maxleng-1):
            break
        if island[costs[index][0]] != island[costs[index][1]]:
            island[costs[index][0]]=1
            island[costs[index][1]]=1
            answer+=costs[index][2]
            count+=1
            index=0
        else:
            index+=1    
            continue
    return answer

print(solution(n, costs))


##5 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]] 15
##5 [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] 8
##4 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]] 9
##5 [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] 104
##6 [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]] 11
##5 [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]] 6
##5 [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]] 8
##5 [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]] 8
