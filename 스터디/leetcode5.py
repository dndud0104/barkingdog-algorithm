s = "bccb"

#설계미스 솔루션
def solution(s):
    answer = ""
    
    for i in range(len(s)):
        left, right = i,i
        tmp = ""
        tmp+=s[i]

        while True:
            if right + 1 >= len(s) or s[i]!= s[right+1]:
                break
            if s[i] == s[right+1]:
                right+=1
                tmp+=s[right]
                
        
        while True:
            if left-1 < 0 or right+1 >= len(s):
                break
            if s[left-1] == s[right+1]:
                left -= 1
                right += 1
                tmp = s[left] + tmp + s[right]
            else:
                break
            
        if len(tmp)>=len(answer):
            answer = tmp
                
    return answer

print(solution(s))



#시간초과 솔루션
##def solution(s):
##    answer = ""
##    print(len(s))
##    for x in range(len(s)):
##        tmp = ""
##        for y in range(x,len(s)):
##            tmp += s[y]
##            if "".join(reversed(tmp)) == s[x:y+1] and len(tmp)>=len(answer):
##                answer = tmp
##    return answer

