def solution(x, n): #my solution
    return [i*x for i in range (1, n+1)]

def solution(x, n): #my solution, but it occurs runtime error.
    answer = range(1, n+1, x)
    return answer