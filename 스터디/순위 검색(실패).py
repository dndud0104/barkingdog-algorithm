#시간초과
#https://school.programmers.co.kr/learn/courses/30/lessons/72412

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]



def solution(infos, query):
    answer = []

    dic_info = {}
    for x in ['java','python','cpp','-']:
        for y in ['backend','frontend','-']:
            for z in ['junior','senior','-']:
                for w in ['pizza','chicken','-']:
                    dic_info[x+y+z+w] = []

    for info in infos:
        info = info.split(" ")
        for lang in [info[0], "-"]:
            for job in [info[1], "-"]:
                for career in [info[2], "-"]:
                    for food in [info[3], "-"]:
                        dic_info[lang + job + career + food].append(int(info[4]))


    
    for a in query:
        count=0
        tmp = a.replace('and','').split()
        for value in dic_info[tmp[0]+tmp[1]+tmp[2]+tmp[3]]:
            if value >= int(tmp[4]):
                count+=1
        answer.append(count)

        

            
    return answer



print(solution(info, query))

##info
##[['java', 'backend', 'junior', 'pizza', '150'],
## ['python', 'frontend', 'senior', 'chicken', '210'],
## ['python', 'frontend', 'senior', 'chicken', '150'],
## ['cpp', 'backend', 'senior', 'pizza', '260'],
## ['java', 'backend', 'junior', 'chicken', '80'],
## ['python', 'backend', 'senior', 'chicken', '50']]
##query
##[['java', 'backend', 'junior', 'pizza', '100'],
## ['python', 'frontend', 'senior', 'chicken', '200'],
## ['cpp', '-', 'senior', 'pizza', '250'],
## ['-', 'backend', 'senior', '-', '150'],
## ['-', '-', '-', 'chicken', '100'],
## ['-', '-', '-', '-', '150']]
