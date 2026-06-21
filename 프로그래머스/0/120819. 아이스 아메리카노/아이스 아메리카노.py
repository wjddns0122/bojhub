def solution(money):
    result = 0
    change = 0
    if money % 5500 == 0:
        result = int(money / 5500)
    else:
        result = int(money // 5500)        
        change = money - (5500 * result)
    answer = [result, change]
    return answer