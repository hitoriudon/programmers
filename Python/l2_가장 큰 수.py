
def solution(numbers): #my
    numbers = [str(i) for i in numbers] # numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers))) # ''.join(numbers) has errors

'''
"1"과 "10"를 대수비교하면 "10"이 더 크고, sort()에 반영되는 건 알고 있었는데...
문제 제한 조건에 1000미만 세 자리 자연수를 보고도 아무 생각이 없었음
테스트케이스에 추가한 '1','10','110'의 대수비교 하기 위해
x*3을 한 다음 비교한다면, 정확히 111010이 나옴. 
'''