def solution(s): #my solution
    tmp = s.lower().split(' ')
    for i in range (len(tmp)):
        tmp[i] = tmp[i].capitalize()
    return ' '.join(tmp)

def solution(s): #advanced
    return ' '.join([word.capitalize() for word in s.split(" ")])


