sub_eng=0
arr1 = input()
arr2 = input()
count = [0 for i in range(26)]
for j in range(len(arr1)):
    count[ord(arr1[j])-97]+=1
for k in range(len(arr2)):
    count[ord(arr2[k])-97]-=1
for m in range(26):
        if count[m]!=0:
            sub_eng+=abs(count[m])
print(sub_eng)
