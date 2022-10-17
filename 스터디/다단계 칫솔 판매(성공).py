#https://school.programmers.co.kr/learn/courses/30/lessons/77486
import math

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]




def solution(enroll, referral, seller, amount):
    answer = []
    price = 100
    multilevel = dict({en:re for en, re in zip(enroll, referral)})
    result = dict({en:0 for en in enroll})
    
    for i in range(len(seller)):
        am = amount[i]*price
        sell = seller[i]
        while True:
            result[sell] += am-am//10
            sell = multilevel[sell]
            am = am//10
            print(sell)
            if am == 0:
                break
            if sell=='-':
                break
    
##    for value in result.values():
##        answer.append(value)
  
    return list(result.values())





print(solution(enroll, referral, seller, amount))
