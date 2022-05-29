def solution(left, right): #my
    answer = 0
    for i in range (right-left+1):
        cnt = 0
        for j in range (1,left+i+1):
            if (left+i)%j==0: cnt += 1
        answer += left+i if cnt%2==0 else (left+i)*(-1)
    return answer

def solution(left, right): #best
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            '''
            약수의 개수가 홀수인 경우는 제곱수인 경우임.
            ex) 25-> 1, 5, 25. 36-> 1, 6, 36
            '''
            answer -= i
        else:
            answer += i
    return answer
