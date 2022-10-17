#https://school.programmers.co.kr/learn/courses/30/lessons/12984

##land = [[1,2,2,2,2,2,2,2,2,2,2],
##        [2,2,2,2,2,2,2,2,2,2,2],
##        [2,2,2,2,2,2,2,2,2,2,2],
##        [2,2,2,2,2,2,2,2,2,2,2],
##        [2,2,2,2,2,2,2,2,2,2,2],
##        [2,2,2,2,2,2,2,2,2,2,2],
##        [2,2,2,2,2,2,2,2,2,2,2],
##        [2,2,2,2,2,2,2,2,2,2,2],
##        [2,2,2,2,2,2,2,2,2,2,2],
##        [2,2,2,2,2,2,2,2,2,2,2],
##        [2,2,2,2,2,2,2,2,2,2,3]]
land = [[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]]
P = 5 #추가비용
Q = 3 #제거비용


def calc(land, mid, P, Q):
    Qcoast = 0
    Pcoast = 0
    for row in land:
        for col in row:
            if col > mid:
                Qcoast += col - mid
            elif col < mid:
                Pcoast += mid - col
    return Qcoast*Q + Pcoast*P

def solution(land, P, Q):
    maxFloor = max(max(land))
    minFloor = min(min(land))
    answer = 0
    while minFloor <= maxFloor:
        print(minFloor, maxFloor)
        mid = (maxFloor + minFloor)//2
        midCoast = calc(land, mid, P, Q)
        upCoast = calc(land, mid+1, P, Q)
        print(midCoast, upCoast)
        if midCoast<=upCoast:
            answer = midCoast
            maxFloor = mid - 1
        else:
            answer = upCoast
            minFloor = mid + 1
    
    return answer


print(solution(land, P, Q))



##def solution(land, P, Q):
##    answer = []
##    
##    for height in range(max(max(land)),-1,-1):
##        tmp = 0
##        for row in land:
##            for col in row:
##                if col < height:
##                    tmp += (height - col)*P
##                elif col == height:
##                    continue
##                elif col > height:
##                    tmp += (col - height)*Q
##        answer.append(tmp)
##        print(height, tmp)
##                    
##    return min(answer)

##def solution(land, P, Q):
##    maxFloor = max(max(land))
##    minFloor = min(min(land))
##    answer = 0
##    while True:
##        print(minFloor,maxFloor)
##        mid = (maxFloor + minFloor)//2
##        if mid == minFloor:
##            answer = Qcoast+Pcoast
##            break
##        Qcoast = 0
##        Pcoast = 0
##        for row in land:
##            for col in row:
##                if col > mid:
##                    Qcoast += col - mid
##                elif col < mid:
##                    Pcoast += mid - col
##        Qcoast *= Q
##        Pcoast *= P
##        if Pcoast > Qcoast:
##            maxFloor = mid
##        elif abs(Qcoast-Pcoast) <= Q or Pcoast < Qcoast:
##            minFloor = mid
##    
##    return answer
