#https://school.programmers.co.kr/learn/courses/30/lessons/92341
import math

def solution(fees, records):
    answer = []
    tmp = []
    dic = {}
    
    for i in range(len(records)):
        split_record = records[i].split()
        split_time = split_record[0].split(':')
        time = int(split_time[0])*60+int(split_time[1])
        if dic.get(str(split_record[1]))==None:
            dic[split_record[1]]=[time,0]
        elif split_record[2] == 'OUT':
            save_time = dic[split_record[1]]
            dic[split_record[1]]=[time-save_time[0],1]
        else:
            save_time = dic[split_record[1]]
            dic[split_record[1]]=[time-save_time[0],0]
            
    for number in dic:
        values = dic.get(number)
        if values[1] == 0:
            dic[number]=[1439-values[0],1]
        values = dic.get(number)    
        if values[0]>fees[0]:
            tmp.append([number, fees[1]+math.ceil((values[0]-fees[0])/fees[2])*fees[3]])
        else:
            tmp.append([number,fees[1]])
     
    tmp = sorted(tmp)
    for i in range(len(tmp)):
        answer.append(tmp[i][1])
    return answer
