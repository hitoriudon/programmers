def solution(arr): #my
    answer=[]
    for i in range (len(arr)-1):
        if arr[i]!=arr[i+1]:
            answer.append(arr[i])
    answer.append(arr.pop())
    return answer

def solution(s): #1st
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

def solution(s): #2nd
    result = []
    for c in s:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result
    