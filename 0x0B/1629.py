def recur(a, b, m):
    if b == 1: #k
        return a % m
    answer = recur(a, b//2, m)
    answer = answer * answer % m
    if b%2 == 0: #2k
        return answer
    return answer * a % m #2k+1


A, B, C = map(int, input().split())
print(recur(A,B,C))
