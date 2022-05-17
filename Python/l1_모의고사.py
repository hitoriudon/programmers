def solution(answers): #my
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    tmp = [0,0,0]
    answer = []
    for i in range (len(answers)):
        if answers[i] == p1[i%5]:
            tmp[0]+=1
        if answers[i] == p2[i%8]:
            tmp[1]+=1
        if answers[i] == p3[i%10]:
            tmp[2]+=1
    maxnum = max(tmp)
    if maxnum == tmp[0]:
        answer.append(1)
    if maxnum == tmp[1]:
        answer.append(2)
    if maxnum == tmp[2]:
        answer.append(3)
    return answer

#enumerate is more better
def solution(answers): #1st
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result