#https://school.programmers.co.kr/learn/courses/30/lessons/42579

genres = ['classic', 'pop', 'classic', 'classic', 'pop'] #장르
plays = [500, 600, 150, 600, 2500] # 재생 횟수


def solution(genres, plays):
    answer = []
    dic_gen = {}
    lst_mus = []
    
    for i,(g,p) in enumerate(zip(genres,plays)): #리스트(인덱스, 장르명, 횟수)
        lst_mus.append([i,g,p])
    print(lst_mus)
    for gen, pl in zip(genres,plays): #딕셔너리(장르명, 횟수 합)
        if gen in dic_gen:
            dic_gen[gen] += pl
        else:
            dic_gen[gen] = pl
            
    sort_d = dict(sorted(dic_gen.items(), key=lambda x: x[1], reverse = True)) #많이 재생된 장르 순 정렬
    sort_m = sorted(lst_mus, key=lambda x: x[2], reverse = True)
    print(sort_d)
    print(sort_m)

    for gen in sort_d:
        count = 0
        for lank in sort_m:
            if gen == lank[1]:
                answer.append(lank[0])
                count+=1
            if count == 2:
                break
    
    return answer


print(solution(genres, plays))
