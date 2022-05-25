def solution(s): #my
    answer=s.split(" ")
    tmp=""
    for i in range (len(answer)):
        for j in range (len(answer[i])):
            if j%2: tmp+=answer[i][j].lower()
            else: tmp+=answer[i][j].upper()
        tmp+=" "
    return tmp[:-1]

def toWeirdCase(s): #best
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

def solution(s): #error.
    answer=s.split()
    tmp=""
    for i in range (len(answer)):
        for j in range (len(answer[i])):
            if j%2: tmp+=answer[i][j].lower()
            else: tmp+=answer[i][j].upper()
        tmp+=" "
    return tmp[:-1]
'''
에러가 계속 나는 이유는. split()처리인 것 같다. 제한 조건에서 공백이 하나 이상인데, 문자열 마지막에 공백이 포함되어 있으면
그 공백까지 출력을 해줘야 해서... split()은 공백을 모두 삭제해버리기 때문에.. split(" ")으로 하니까 딱 됨.
'''