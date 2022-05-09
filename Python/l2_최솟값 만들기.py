def solution(A,B): #my
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range (len(A)):
        answer = answer + A[i] * B[i]
    return answer

def solution(A,B): #1st
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))