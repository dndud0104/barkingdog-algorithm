user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id1 = ["fr*d*", "abc1**"]
banned_id2 = ["*rodo", "*rodo", "******"]
banned_id3 = ["fr*d*", "*rodo", "******", "******"]

db = []
def compare(id1, id2):
    if len(id1)!=len(id2):
        return False
    for x,y in zip(id1, id2):
        if x=='*' or x==y:
            continue
        else:
            return False
    return True

def solution(user_id, banned_id,tempQueue=[],isItHead=True):
    if len(banned_id)==0:
        #print(tempQueue)
        tempQueue.sort()
        #print(tempQueue)
        db.append(''.join(tempQueue))
        print(db)
        return
    del_id = banned_id.pop()
    for temp_id in user_id:
        #print(del_id, temp_id)
        if compare(del_id, temp_id):
            temp_user_id = user_id[:]
            temp_user_id.remove(temp_id)
            tempQueue_=tempQueue[:]
            tempQueue_.append(temp_id+'/')
            #print(tempQueue_)
            solution(temp_user_id,banned_id[:],tempQueue_,False)
    if isItHead:
        return len(set(db))

print(solution(user_id,banned_id2))
    
