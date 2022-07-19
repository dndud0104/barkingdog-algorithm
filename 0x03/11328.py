N = int(input())

for i in range(N):
    cham=1
    arr1, arr2 = map(str, input().split())
    count1 = [0 for i in range(1000)]
    count2 = [0 for i in range(1000)]
    for j in range(len(arr1)):
        count1[ord(arr1[j])-97]+=1
    for k in range(len(arr2)):
        count2[ord(arr2[k])-97]+=1
    for m in range(26):
        if count1[m]!=count2[m]:
            cham=0
            break
    if cham == 1:
        print("Possible")
    else:
        print("Impossible")
