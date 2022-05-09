def solution(x): #my solution
    answer = 0
    lst=list(str(x))
    for i in range (len(lst)):
        answer+=int(lst[i])
    if x % answer == 0:
        return True
    else:
        return False

def Harshad(n): #1st solution
    return n % sum([int(c) for c in str(n)]) == 0