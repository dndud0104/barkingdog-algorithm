#함수의 정의
def func(a,b,n):#시작, 끝, 원판
    
#base condition
#n이 1일때 반환
    if n == 0:
        #print(a, b)
        return
    
#재귀식
#a도 b도 아닌 기둥의 번호는 6-a-b
#n-1개의 원판을 기둥 a에서 기둥 6-a-b로 옮긴다
    func(a,6-a-b,n-1)
#n번 원판을 기둥 a에서 기둥 b로 옮긴다
    print(a, b)
#n-1개의 원판을 기둥 6-a-b에서 기둥 b로 옮긴다
    func(6-a-b,b,n-1)


K = int(input())
print((1 << K) - 1)
func(1,3,K)
