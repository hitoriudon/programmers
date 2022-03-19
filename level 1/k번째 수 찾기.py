def solution(array, commands): #my solution
    answer=[]
    for i in range (len(commands)):
        tlist=[]
        for j in range (commands[i][0], commands[i][1]+1):
            tlist.append(array[j-1])
        tlist.sort()
        k=tlist[commands[i][2]-1]
        answer.append(k)
    return answer

def solution(array, commands): #2nd solution
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

def solution(array, commands): #1st solution
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))