#https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        tmp1 = []
        tmp2 = []
        mid_result = ""
        count = 0
        while arr1[i]>0:
            tmp1.append(arr1[i]%2)
            arr1[i]//=2
            count+=1
        if(count!=n):
            for j in range(n-count):
                tmp1.append(0) 
        count = 0        
        while arr2[i]>0:
            tmp2.append(arr2[i]%2)
            arr2[i]//=2
            count+=1
        if(count!=n):
            for j in range(n-count):
                tmp2.append(0)  
        tmp1.reverse()
        tmp2.reverse()
        for k in range(n):
            if(tmp1[k]!=tmp2[k]):
                mid_result+="#"
            elif(tmp1[k]==tmp2[k] and tmp1[k]==0):
                mid_result+=" "
            else:
                mid_result+="#"
                
        answer.append(mid_result)

    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n,arr1,arr2))
