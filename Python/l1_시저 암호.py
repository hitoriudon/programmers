def solution(s, n): #my
    ups = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lows = "abcdefghijklmnopqrstuvwxyz"
    answer = []
    for t in s:
        if t in ups: answer.append(ups[(ups.index(t)+n)%26])
        elif t in lows: answer.append(lows[(lows.index(t)+n)%26])
        else: answer+=' '
    return ''.join(answer)