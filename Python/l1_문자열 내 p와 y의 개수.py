def solution(s): #my...
    answer = 0
    for i in s:
        if i == 'P' or i == 'p':
            answer+=1
        if i == 'y' or i == 'Y':
            answer-=1
    if answer == 0:
        return True
    else: 
        return False
    
def solution(s): #1st
    return s.lower().count('p') == s.lower().count('y')