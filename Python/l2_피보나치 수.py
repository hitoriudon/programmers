def solution(n): #my
    fibo = [0,1,1]
    for i in range (3,n+1):
        fibo.append((fibo[i-2]+fibo[i-1])%1234567)
    return fibo[-1]

def solution(n): #runtime error
    return 0 if n==0 else 1 if n==1 else (solution(n-1)+solution(n-2))%1234567

def fibonacci(num): #1st
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a