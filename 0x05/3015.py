#시간초과

N = int(input())

line = []
pair = []
count = 0

for i in range(N):
    line.append(int(input()))
    if not pair:
        pair.append([0,line.pop()])
    else:
        while pair and pair[-1][1] < line[-1]:
            tmp = pair.pop()
            if tmp[0] >= 2:
                count+=tmp[0]
            else:
                count+=1
        if not pair:
            pair.append([0, line.pop()])
        elif pair[-1][1] > line[-1]:
            pair.append([1, line.pop()])
            count+=1
        elif pair[-1][1] == line[-1]:
            count+=1
            tmp2 = pair[-1][0]
            pair[-1][0] = 1
            pair.append([tmp2+1, line.pop()])


print(count)
