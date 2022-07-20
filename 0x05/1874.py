##n = int(input())
n = 8
point = 1
##lst = []
lst = [4,3,6,8,7,5,2,1]
answer = ''
check = True
tmp = []

##for i in range(n):
##    lst.append(int(input()))

for num in lst:
    if num >= point:
        for i in range(point, num+1):
            tmp.append(i)
            answer+='+\n'
            point+=1
    if tmp[-1] == num:
        tmp.pop()
        answer+='-\n'
    else:
        check=False
        print("NO")
        break
        
if check:
    print(answer[0:-1])
    
        
