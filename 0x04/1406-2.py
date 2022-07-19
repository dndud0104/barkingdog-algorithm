#스택

##Left = []
##Right = []
##word = input()
##
##for i in word:
##    Left.append(i)


#input()보다 sys.stdin.readline()이 더 빠르다고함
#rstrip()을 쓰지 않으면 list에 \n이 포함됨
import sys
Right = []
#바로 list에 입력 가능
Left = list(sys.stdin.readline().rstrip())

##import sys
##Right = []
##Left = list(input())

M = int(input())
for i in range(M):
    op = lsys.stdin.readline().split()
    if op[0]=="L" and Left:
        Right.append(Left.pop())
    elif op[0]=="D" and Right:
        Left.append(Right.pop())
    elif op[0]=="B" and Left:
        Left.pop()
    elif op[0]=="P":
        Left.append(op[1])

##for i in Left:
##    answer+=i
##for i in range(len(Right)):
##    answer+=Right.pop()
##for문으로pop 하는것보다는 join이 더 빠르다고 함

#Right.reverse는 리턴값이 없어 오류?
#reversed(Right)는 뒤집어진 list를 리턴
print("".join(Left+list(reversed(Right))))
#혹은
##Left.extend(list(reversed(Right)))
##print("".join(Left))

