from itertools import *
from collections import Counter

##orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
##course = [2,3,4]

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

##orders = ["XYZ", "XWY", "WXA"]
##course = [2,3,4]



def solution(orders, course):
    answer = []

    for num in course:#조합을 위한 수를 먼저 뽑고
        result = []
        for menu in orders:#주문 메뉴에서 뽑은 수 만큼 조합
            tmp = combinations(sorted(menu), num)
            result += tmp#가능한 조합들을 모두 저장
        tmp2 = Counter(result)#조합들의 중복 개수를 셈
        print(tmp2)


##        if len(tmp2) != 0 and max(tmp2.values()) != 1:
##            answer += [''.join(tmp3) for tmp3 in tmp2 if tmp2[tmp3] == max(tmp2.values())]
        #둘다 동일한 결과, 위가 좀더 간결
        if len(tmp2)!=0 and max(tmp2.values())!=1:
            for tmp3 in tmp2:
                print(tmp3)
                if tmp2[tmp3] == max(tmp2.values()):#Counter의 max와 tmp3의 값이 같다면
                    answer.append("".join(tmp3))#결과에 join하여 tmp3을 저장
    
    return sorted(answer)#course의 모든 수의 조합을 추가하고 정렬하여 출력


print(solution(orders, course))


#시간초과, 모든 경우의 수를 다 셈
#주문에 없는 조합도 모두 세서 오래걸림
##def solution(orders, course):
##    answer = []
##    result = []
##    tmp = list(sorted(set("".join(orders))))
##   
##    for j in course:
##        tmp2 = list(combinations(tmp, j))
##
##        for k in tmp2:
##            count_set=0
##            
##            for menu in orders:
##                count = 0
##                
##                for i in k:
##                    if i in menu:
##                        count+=1
##                    else:
##                        break
##                    
##                if count == j:
##                    count_set+=1
##                    
##            if count_set >=2:
##                if not result:
##                    result.append([count_set,"".join(k)])
##                    continue
##                
##                if count_set < result[-1][0]:
##                    continue
##                elif count_set == result[-1][0]:
##                    result.append([count_set,"".join(k)])
##                    continue
##                
##                while count_set > result[-1][0]:
##                    result.pop()
##                    if not result:
##                        break
##                result.append([count_set,"".join(k)])
##
##        result.append([0,0])
##        
##    for k in result:
##        if k[0]>0:
##            answer.append(k[1])
##            
##    answer = sorted(answer)     
##             
##    return answer
