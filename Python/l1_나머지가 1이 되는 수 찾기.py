def solution(n): #my
    for i in range (n,1,-1):
        if n%i == 1:
            answer = i
    return answer

def solution(n): #creative
    return [x for x in range(1,n+1) if n%x==1][0]

