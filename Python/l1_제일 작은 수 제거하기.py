def solution(arr): #my
    arr.remove(min(arr))
    return [-1] if len(arr)==0 else arr