pre = [-1 for i in range(600005)]
nxt = [-1 for i in range(600005)]
dat = [-1 for i in range(600005)]
unused = 1

def erase(addr):
    if (nxt[addr] != -1):
        pre[nxt[addr]] = pre[addr]
    nxt[pre[addr]] = nxt[addr]

def insert(addr, code):
    global unused
    dat[unused] = code
    pre[unused] = addr
    if(nxt[addr]==-1):
        nxt[addr] = unused
    else:
        nxt[unused] = nxt[addr]
        nxt[addr] = unused
        pre[nxt[unused]] = unused
    unused+=1


word = input()
cursor = len(word)
for i in range(cursor):
    dat[unused]=word[i]
    nxt[i]=unused
    pre[unused]=i
    unused+=1
    
M = int(input())
for i in range(M):
    op = input()
    if op=="L":
        if(pre[cursor] != -1):
            cursor = pre[cursor]
    elif op=="D":
        if(nxt[cursor] != -1):
            cursor = nxt[cursor]
    elif op=="B":
        if(pre[cursor] != -1):
            erase(cursor)
            cursor = pre[cursor]
    else:
        code = input()
        insert(cursor, code)
        cursor = nxt[cursor]

cur = nxt[0]
while cur != -1:
    print(dat[cur], end='')
    cur = nxt[cur]
            
            
        
        
    


    
