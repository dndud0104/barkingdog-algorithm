from itertools import *

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id1 = ["fr*d*", "abc1**"]
banned_id2 = ["*rodo", "*rodo", "******"]
banned_id3 = ["fr*d*", "*rodo", "******", "******"]
##banned_id = ["******"]



def solution(user_id, banned_id):
    answer = 0
    lst_ban = []
    for b_id in banned_id:
        tmp = []
        for u_id in user_id:
            if len(b_id) != len(u_id):
                continue
            else:
                ilchi = True
                for i in range(len(b_id)):
                    if b_id[i] == u_id[i]:
                        continue
                    elif b_id[i] == '*':
                        continue
                    else:
                        ilchi = False
                        break
                if ilchi:
                    tmp.append(u_id)
                    #lst_ban.append(u_id)
        lst_ban.append(tmp)

    
    #print(list(product(*lst_ban)))
    caselist = list(product(*lst_ban))
    items = list(set([tuple(set(item)) for item in caselist]))
    #print(items)
## 
    for i in items:
        if len(set(i)) == len(banned_id):
            #print(set(i))
            answer+=1
    
        
    return answer






print(solution(user_id, banned_id1))
print(solution(user_id, banned_id2))
print(solution(user_id, banned_id3))
