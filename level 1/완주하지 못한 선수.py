def solution(participant, completion): #my solution, not using hash...
    participant.sort()
    completion.sort()
    for i in range(len(completion)): 
        if(participant[i] != completion[i]): 
            return participant[i]
    return participant[len(participant)-1]
    
def solution(participant, completion): #my wrong answer, completed only 2 conditions.
    answer = ''
    for i in participant:
        if i not in completion:
            answer= i
    return answer

def solution(participant, completion): #my wrong answer, test case is okay but time is over
    for i in participant:
        for i in completion:
            if i in completion:
                participant.remove(i)
    answer=participant[0]
    return answer

def solution(participant, completion): #hash
    hashDict={}
    sumHash=0
    for i1 in participant:
        hashDict[hash(i1)]=i1
        sumHash+=hash(i1)
    for i2 in completion:
        sumHash-=hash(i2)
    return hashDict[sumHash]
        

