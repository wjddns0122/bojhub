def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s = sorted(s, key=lambda x: len(x))
    
    s = [list(map(int, tup.split(','))) for tup in s]
    
    for tup in s:
        for i in answer:
            if i in tup:
                tup.remove(i)
        answer.append(tup[0])
        
    return answer