def calculate_score(quiz_result):
    score = 0
    current_streak = 0

    for answer in quiz_result:
        if answer == 'O':
            current_streak += 1
            score += current_streak
        else:
            current_streak = 0

    return score

# 테스트 케이스 개수 입력
test_cases = int(input())

# 각 테스트 케이스에 대해 점수 계산 및 출력
for _ in range(test_cases):
    quiz_result = input().strip()  # 문자열 입력받기
    print(calculate_score(quiz_result))  # 점수 출력