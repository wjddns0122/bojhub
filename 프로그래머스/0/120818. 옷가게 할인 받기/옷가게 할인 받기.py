def solution(price):
    if price >= 500000:
        answer = price - (price / 10 * 2)  # 20% 할인
    elif price >= 300000:
        answer = price - (price / 10)      # 10% 할인
    elif price >= 100000:
        answer = price - (price / 100 * 5) # 5% 할인
    else:
        answer = price
    return int(answer)
