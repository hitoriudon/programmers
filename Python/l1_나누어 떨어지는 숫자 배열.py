def solution(arr, divisor): #my
    arr = sorted(list(filter(lambda x: x%divisor==0, arr)))
    return [-1] if len(arr)==0 else arr
    #[x for x in arr if x%divisor==0]