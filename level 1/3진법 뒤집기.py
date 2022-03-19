def solution(n): #my solution
    rev_base = ''
    answer = 0
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod) #like a stack
    for i in range (len(rev_base)):
        k= int(rev_base[i])
        answer+= k* 3**(len(rev_base)-i-1)
    return answer

def solution(n): #1st solution
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3
    answer = int(tmp, 3)
    return answer