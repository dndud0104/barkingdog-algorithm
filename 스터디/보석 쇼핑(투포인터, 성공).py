#투포인터
#https://school.programmers.co.kr/learn/courses/30/lessons/67258
from collections import deque

#gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
#gems = ["AA", "AB", "AC", "AA", "AC"]
#gems = ["XYZ", "XYZ", "XYZ"]
#gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

#gems=["A","A","A","B","B"] #[3,4]
gems=["A"] #[1,1]
#gems=["A","B","B","B","B","B","B","C","B","A"] #[8,10]
#gems=["A", "B", "C", "B", "F", "D", "A", "F", "B", "D", "B"] #[3, 7] 

#투포인터 알고리즘
def solution(gems):
    answer = []
    s, e = 0, 0#시작점 끝점
    dist = 100000#최대 길이
    dic_gem = {}
    total = len(set(gems))#중복을 제거한 보석의 개수


    while True:
        if len(dic_gem) == total:
            if e-s<dist:#최대 길이보다 짧으면
                dist = e-s
                answer=[s+1, e]
                
            if dic_gem[gems[s]] == 1:#1개 남았을때
                del dic_gem[gems[s]]
                s+=1
            else:#2개 이상 남았을때
                dic_gem[gems[s]]-=1
                s+=1
            
                
        elif e == len(gems):#끝점이 마지막 값에 도달하면
            break
        else:
            if gems[e] in dic_gem:#dic에 있으면 +1
                dic_gem[gems[e]]+=1
            else:#없으면 새로운 키,값 추가
                dic_gem[gems[e]]=1
            e+=1
 
    return answer


print(solution(gems))

#실패작
##def solution(gems):
##    answer = []
##    que = deque([])
##    tmp = dict({gem: False for gem in set(gems)})
##    print(tmp)
##    que.append([gems[0],1])
##    tmp[gems[0]] = True
##    count = 1
##    for i in range(1, len(gems)):
####        if count == len(tmp):
####            break
##        print(que, i)
##        if tmp[gems[i]] == False:
##            que.append([gems[i],i+1])
##            tmp[gems[i]] = True
##            count += 1 
##        elif que[0][0] == gems[i]:
##            que.popleft()
##            que.append([gems[i],i+1])
##        elif que[-1][0] == gems[i]:
##            que.pop()
##            que.append([gems[i],i+1])
##        
##    answer.append(que[0][1])
##    answer.append(que[-1][1])
##    print(que)
##    print(tmp)
##    return answer

#효율성 테스트 시간초과 3개
##def solution(gems):
##    answer = []
##    cw=0#모든 보석의 포함 여부확인
##    count = 1#인덱스 대신 값
##    min_dist = 100000
##
##    tmp = {}
##    count_word = {}
##    tmp_len = len(set(gems))
##    if tmp_len==len(gems):
##        return [1, tmp_len]
##    
##    for gem in gems:
##        if gem not in count_word:   
##            cw+=1
##
##        count_word[gem]=count
##        
##        if cw==tmp_len:
##            dist = count - min(count_word.values())
##            if dist < min_dist:
##                answer = [min(count_word.values()), count]
##                min_dist = dist
##        count+=1
## 
##    return answer
