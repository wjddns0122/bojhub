function solution(s) {
    let a = 0;
    let b = 0;
    var answer = '';
    if (s.length % 2 === 1) {
        a = parseInt(s.length / 2);
        answer = s[a];
    } else {
        a = parseInt(s.length / 2) - 1;
        b = parseInt(s.length / 2);
        answer = s[a] + s[b]
    }
    return answer;
}