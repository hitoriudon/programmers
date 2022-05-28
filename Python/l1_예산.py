def solution(d, budget): #my
    answer = 0
    if sum(d)==budget:
        answer = len(d)
    else:
        for i in sorted(d):
            if budget >= i:
                budget -= i
                answer +=1
    return answer

def solution(d, budget): #another. time complexity?
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)