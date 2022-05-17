def solution(n): #my
    n2= list(str(n))
    n2.sort(reverse=True)
    return int(''.join(str(i) for i in n2))