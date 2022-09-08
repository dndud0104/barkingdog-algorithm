#1. 함수 정의
def Z(n,r,c):
#2. base condition
    if n == 0:
        return 0
#3. 재귀식
    if r < 2**(n-1) and c < 2**(n-1):
        return Z(n-1,r,c)
    if r < 2**(n-1) and c >= 2**(n-1):
        return 2**(n-1)*2**(n-1) + Z(n-1,r,c-2**(n-1))
    if r >= 2**(n-1) and c < 2**(n-1):
        return 2*2**(n-1)*2**(n-1) + Z(n-1,r-2**(n-1),c)
    if r >= 2**(n-1) and c >= 2**(n-1):
        return 3*2**(n-1)*2**(n-1) + Z(n-1,r-2**(n-1),c-2**(n-1))



N, r, c = map(int, input().split())

print(Z(N,r,c))
