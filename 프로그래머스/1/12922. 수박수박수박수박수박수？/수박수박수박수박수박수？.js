function solution(n) {
    var answer = '';
    let i = 0;
    while (i < n) {
        i += 1
        if (i % 2 === 1) {
            answer += '수';
        } else if (i % 2 === 0) {
            answer += '박';
        }
    }
    return answer;
}

