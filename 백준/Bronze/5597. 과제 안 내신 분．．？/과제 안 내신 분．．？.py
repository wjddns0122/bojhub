# 학생 번호를 저장할 리스트
students = []

# 28명의 학생 번호 입력받기
for _ in range(28):
    a = int(input())
    students.append(a)

# 모든 학생 번호 (1부터 30까지)
all_students = set(range(1, 31))

# 입력받은 학생 번호를 set으로 변환
entered_students = set(students)

# 누락된 학생 번호 찾기
missing_students = list(all_students - entered_students)

# 결과 출력
print(sorted(missing_students)[0])  # 첫 번째 누락된 학생 번호
print(sorted(missing_students)[1])  # 두 번째 누락된 학생 번호