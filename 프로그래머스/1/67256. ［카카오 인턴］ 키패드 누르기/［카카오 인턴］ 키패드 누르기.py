def solution(numbers, hand):
    answer = ''
    left_pos = 10
    right_pos = 12

    for i in range(len(numbers)):
        num = numbers[i]

        # 1, 4, 7 인 경우 (오른손인 경우)
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            left_pos = num

        # 3, 6, 9 인 경우 (왼손인 경우)
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            right_pos = num

        # 2, 5, 8, 0인 경우 (가까운 순)
        else:
            # 0은 계산을 쉽게 하기 위해 11로 바꾼 후
            if num == 0:
                num = 11

            # 현재 내 왼손/오른손 위치와 목표 숫자 계산
            # 맨허튼 거리 이용 (숫자 차이를 3으로 나눈 몫) + (나눈 거리)
            dist_l = abs(num - left_pos) // 3 + abs(num - left_pos) % 3
            dist_r = abs(num - right_pos) // 3 + abs(num - right_pos) % 3

            if dist_l < dist_r:
                answer += 'L'
                left_pos = num
            elif dist_r < dist_l:
                answer += 'R'
                right_pos = num
            else:
                if hand == "right":
                    answer += 'R'
                    right_pos = num
                else:
                    answer += "L"
                    left_pos = num

        
    return answer