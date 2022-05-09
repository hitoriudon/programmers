def solution(n): #my
    answer = ''
    for i in range (0,n):
        if i%2==0:
            answer+='수'
        else:
            answer+='박'
    return answer

def water_melon(n): #1st. There is an opinion about using unnessary memory spaces.
    s = "수박" * n
    return s[:n]