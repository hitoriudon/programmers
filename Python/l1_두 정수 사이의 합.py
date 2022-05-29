def solution(a, b): #my
    return sum([i for i in range (a,b+1,1)]) if a<=b else sum([i for i in range (b,a+1,1)])

def adder(a, b): #best
    return (abs(a-b)+1)*(a+b)//2

def adder(a, b): #best 2
    if a > b: a, b = b, a #no temp in python
    return sum(range(a,b+1))