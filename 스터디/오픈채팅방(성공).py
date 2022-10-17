#https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    id_nick = {}
    
    for i in range(len(record)):
        tmp = record[i].split()
        if tmp[0]=="Enter" or tmp[0]=="Change":
            id_nick[tmp[1]]=tmp[2]
    for i in range(len(record)):
        tmp = record[i].split()
        if tmp[0]=="Enter":
            answer.append(id_nick[tmp[1]]+"님이 들어왔습니다.")
        elif tmp[0]=="Leave":
            answer.append(id_nick[tmp[1]]+"님이 나갔습니다.")    
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
