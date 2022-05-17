def solution(s): #my...
    answer=''
    i=0
    while i<len(s):
        if ord(s[i])<=57:
            answer+=s[i]
            i+=1
        elif s[i]=='z':
            answer+='0'
            i+=4
        elif s[i]=='o':
            answer+='1'
            i+=3
        elif s[i:i+2]=='tw':
            answer+='2'
            i+=3
        elif s[i:i+2]=='th':
            answer+='3'
            i+=5
        elif s[i:i+2]=='fo':
            answer+='4'
            i+=4
        elif s[i:i+2]=='fi':
            answer+='5'
            i+=4
        elif s[i:i+2]=='si':
            answer+='6'
            i+=3
        elif s[i:i+2]=='se':
            answer+='7'
            i+=5
        elif s[i]=='e':
            answer+='8'
            i+=5
        elif s[i]=='n':
            answer+='9'
            i+=4
    return int(answer)

def solution(s): #1st 
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

def solution(s): #2nd
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
    