#my
def GCD(n, m): 
    tmp=n
    while tmp!=0:
        n=tmp
        tmp=m%n
        m=n
    return n
def LCM(n, m):
    return n*m/GCD(n,m)
def solution(n, m):    
    return [GCD(n,m),LCM(n,m)]

#1st
def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer