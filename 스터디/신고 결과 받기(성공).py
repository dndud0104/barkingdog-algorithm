#https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    #set 자료형
    #중복되는 데이터가 사라짐
    report = list(set(report))
    #dictionary 자료형
    #id_list의 값을 id에 받아와 id와 0을 세트로 묶어줌
    id_dict = {id : 0 for id in id_list}
    report_dict = {id : 0 for id in id_list}
    
    #report의 수만큼 반복하면서 신고당한 횟수를 dictionary 자료형에 더함
    #dictionary 자료형은 key값으로 자료를 검색
    #set으로 중복을 제거했기 때문에 가능
    for i in range(len(report)):
        report_dict[report[i].split()[1]]+=1
    
    #정지 기준 횟수보다 많은 유저가 있으면 해당 유저를 신고한 유저에게 메일을 보냄
    for i in range(len(report)):
        if report_dict[report[i].split()[1]] >= k:
            id_dict[report[i].split()[0]]+=1
    
    return list(id_dict.values())
