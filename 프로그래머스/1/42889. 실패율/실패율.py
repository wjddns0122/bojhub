# 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

# 전체 스테이지 개수가 N이라고 주어질때 stage 별 통과한 사람들의 실패율을 구해보자

def solution(N, stages):
    answer = []
    
    # 1. 스테이지를 오름차순 정렬 (1번부터 순서대로 처리하기 위해)
    stages = sorted(stages)
    
    # 2. 전체 플레이어 수를 길이를 통해 구함
    total_players = len(stages)
    
    # 3. 각 스테이지별 실패율 계산
    idx = 0  # stages 리스트 탐색용 인덱스
    
    for stage in range(1, N + 1):
        # 현재 스테이지에 머물러 있는 사람 수 카운트 (while문 사용!)
        count = 0
        while idx < len(stages) and stages[idx] == stage:
            count += 1
            idx += 1
        
        # 실패율 계산
        if total_players == 0:
            fail_rate = 0
        else:
            fail_rate = count / total_players
        
        answer.append((stage, fail_rate))
        
        # 다음 스테이지로 넘어갈 때 현재 스테이지에 머문 인원 제외
        total_players -= count
    
    # 4. 실패율 내림차순 정렬, 같으면 작은 번호 스테이지가 먼저
    answer.sort(key=lambda x: (-x[1], x[0]))
    
    # 스테이지 번호만 추출
    return [stage for stage, _ in answer]