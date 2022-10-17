#https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = 1000
    
    if len(s)==1:
        return 1
    
    for i in range(1, len(s)//2+1):
        word =''
        count = 1
        for j in range(0,len(s),i):
            #print(s[j:j+i])
            tmp = s[j:j+i]
            if tmp == s[j+i:j+2*i]:
                #print(tmp)
                count+=1
            else:
                if count>1:
                    word+=str(count)
                    word+=tmp
                else:
                    word+=tmp
                count=1
        #print(len(word))
        if answer>len(word):
            answer=len(word)
    return answer

s = "aabbaccc"
print(solution(s))
