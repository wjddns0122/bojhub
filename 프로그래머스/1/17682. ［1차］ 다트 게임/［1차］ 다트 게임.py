def solution(dartResult):
    scores = []
    temp_num = 0
    
    # 문자열을 하나씩 순회
    for i in range(len(dartResult)):
        char = dartResult[i]
        
        # 1. 숫자 처리 (0~10)
        if char.isdigit():
            # 만약 10인 경우 (앞글자가 1이고 현재가 0일 때)
            if char == '0' and i > 0 and dartResult[i-1] == '1':
                temp_num = 10
            else:
                temp_num = int(char)
                
        # 2. 보너스 처리 (S, D, T)
        elif char == 'S':
            scores.append(temp_num ** 1)
        elif char == 'D':
            scores.append(temp_num ** 2)
        elif char == 'T':
            scores.append(temp_num ** 3)
            
        # 3. 옵션 처리 (*, #)
        elif char == '*':
            # 스타상: 현재 점수 2배
            scores[-1] *= 2
            # 이전 점수가 있다면 그것도 2배
            if len(scores) >= 2:
                scores[-2] *= 2
        elif char == '#':
            # 아차상: 현재 점수 마이너스
            scores[-1] *= -1
            
    return sum(scores)