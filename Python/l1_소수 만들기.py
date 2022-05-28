from itertools import combinations #my
def solution(nums): 
    answer = 0
    array = [True for _ in range (3001)] 
    for i in range(2, int(3000**0.5)+1):
        if array[i] == True:
            j = 2
            while i * j <= 3000:
                array[i * j] = False
                j += 1
    primes = [i for i in range (2, 3000) if array[i]]
    combi = list(combinations(nums, 3))
    for c in combi:
        if sum(c) in primes:
            answer+=1
    return answer

from itertools import combinations #best
def prime_number(x):
    answer = 0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            answer+=1
    return 1 if answer==1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums,3)])