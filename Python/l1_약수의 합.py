def solution(n): #my
    return sum([i for i in range (1,n+1) if n%i==0])

def solution(num): #lambda
    return sum(filter(lambda x: num % x == 0, range(1, num + 1)))