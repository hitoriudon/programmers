def solution(dartResult): #terrible 
    answer = []
    p = 0
    for i in range (len(dartResult)):
        if p == 1:
            p = 0
            continue
        if '0'<=dartResult[i]<='9':
            if dartResult[i]=='1' and dartResult[i+1]=='0': 
                answer.append(10)
                p+=1
            else: answer.append(int(dartResult[i]))
        elif dartResult[i]=='S': pass
        elif dartResult[i]=='D': answer[-1] = answer[-1]**2
        elif dartResult[i]=='T': answer[-1] = answer[-1]**3
        elif dartResult[i]=='*':
            if len(answer)>=2: answer[-2], answer[-1] = answer[-2]*2, answer[-1]*2
            else: answer[-1] = answer[-1]*2 
        else: answer[-1] = answer[-1] *(-1)
    return sum(answer)
