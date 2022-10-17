#https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    eng_num = ["zero","one","two","three","four","five", "six","seven","eight","nine"]
    
    for num in eng_num:
        s = s.replace(num,str(eng_num.index(num)))
    
    return int(s)

s = "one4seveneight"
print(solution(s))
