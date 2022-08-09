from collections import deque
from collections import Counter
import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    toggle = False
    #입력부
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip()) 
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    if n == 0:
        arr = deque()
    
    #처리부
    flag = 0
    for op in p:
        if op == 'R':
            flag+=1
        elif arr and flag%2==0:
            arr.popleft()
        elif arr and flag%2==1:
            arr.pop()
        else:
            toggle = True
            break
    if toggle:
        print("error")
    elif flag%2==0:
        print("["+",".join(arr)+"]")
    else:
        arr = reversed(arr)
        print("["+",".join(arr)+"]")


#시간초과
##for i in range(T):
##    toggle = False
##    #입력부
##    p = sys.stdin.readline().rstrip()
##    n = int(sys.stdin.readline().rstrip()) 
##    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
##
##    if n == 0:
##        arr = deque()
##    
##    #처리부
##    for op in p:
##        if op == 'R':
##            arr = deque(reversed(arr))
##        elif arr:
##            arr.popleft()
##        else:
##            toggle = True
##            break
##    if toggle:
##        print("error")
##    else:
##        print("["+",".join(arr)+"]")

