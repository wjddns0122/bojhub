a = int(input())
results = []

for _ in range(a):
    data = list(map(int, input().split()))
    count_students = data[0]  # 첫 번째 숫자는 학생 수
    scores = data[1:]  # 나머지는 점수
    total = sum(scores)
    cal = total / count_students
    count = sum(1 for score in scores if score > cal)
    
    cal2 = (count / count_students) * 100
    results.append(f"{cal2:.3f}%")

for result in results:
    print(result)