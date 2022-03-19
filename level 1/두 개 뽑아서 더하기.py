def solution(numbers): #my solution
    tlist = []
    for i in range (len(numbers)):
        for j in range (i+1, len(numbers)):
            temp= numbers[i]+numbers[j]
            tlist.append(temp)
    answer=[]
    for i in tlist:
        if i not in answer:
            answer.append(i)
    answer.sort()
    return answer

def solution(numbers): #1st solution
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer))) 
#set first, and list again -> it can eliminated some duplicates.