def solution(strings, n): #my
    strings.sort()
    return sorted(strings, key=lambda x: x[n])

def solution(strings, n): #sorted 2 key. it has a priority (x[n] -> x)
    return sorted(strings, key=lambda x: (x[n], x))

def solution(strings, n): #0.5 sol
    return sorted(strings, key=lambda x: x[n:])