#https://school.programmers.co.kr/learn/courses/30/lessons/17676

lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]

def solution(lines):
    answer = 0
    if len(lines)==1:
        return 1
    
    end = []
    start = []

    for i in range(len(lines)):
        tmp = lines[i].split()
        end_h = int(tmp[1][0:2])
        end_m = int(tmp[1][3:5])
        end_s = float(tmp[1][6:])
        end.append((3600*end_h+60*end_m+end_s))
        time = float(tmp[2][0:-1])
        
        start.append(end[i] - time + 0.001)

    print(start,end)
    for i in range(len(lines)):
        count = 0
        for j in range(i,len(lines)):
            if end[i]+1 > start[j]:
                count+=1
        print(count)
        answer = max(answer,count)

                
##    for i in range(len(lines)):
##        print(str(start[i])+'--'+str(end[i]))
##        print(str(start_h[i])+':'+str(start_m[i])+':'+str(start_s[i]))
##        print(str(end_h[i])+':'+str(end_m[i])+':'+str(end_s[i]))
    
    return answer

print(solution(lines))


