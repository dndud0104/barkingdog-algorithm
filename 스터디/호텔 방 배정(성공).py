#https://school.programmers.co.kr/learn/courses/30/lessons/64063

import sys
limit_number = 15000 #재귀횟수를 제한해제
sys.setrecursionlimit(limit_number)

k = 10
room_number = [1,3,4,1,3,1]
dic = {}

def findRoom(room):
    print(dic)
    if not room in dic.keys():#dic에 room 번호가 없으면
        dic[room] = room+1 #room번호를 키로 다음 방 번호를 벨류로 저장
        return room #방번호 리턴
    else:
        next_room = dic[room] #키 room이 가리키는 값을 저장
        ret_room =  findRoom(next_room) #다음방 번호가 비어있는지 확인하면서 재귀
        dic[room] = ret_room #room번호를 키로 ret_room 번호를 벨류로 저장
        return ret_room

def solution(k, room_number):
    answer = []

    for i in room_number:
        answer.append(findRoom(i))
    
    return answer

print(solution(k,room_number))
print(dic)

1,3
3,5
4,5
2,3
5,6

#효율성 개 작살
##def solution(k, room_number):
##    answer = []
##    empty = [i+1 for i in range(k)]
##    
##    for i in room_number:
##        if i in empty:
##            empty.remove(i)
##            answer.append(i)
##        else:
##            tmp = i
##            while True:
##                tmp+=1
##                if tmp in empty:
##                    empty.remove(tmp)
##                    answer.append(tmp)
##                    break
##  
##    return answer

##테스트 18 〉	통과 (9.49ms, 10.3MB)
##테스트 19 〉	통과 (27.15ms, 10.3MB)
##테스트 20 〉	통과 (38.04ms, 10.4MB)
##테스트 21 〉	통과 (238.62ms, 10.4MB)
##테스트 22 〉	통과 (254.99ms, 10.3MB)
##테스트 23 〉	통과 (54.80ms, 10.4MB)
##테스트 24 〉	통과 (250.08ms, 10.2MB)
