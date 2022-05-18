def solution(s): #my
    stack = []
    for i in s:
        stack.append(i)
        if len(stack)>=2 and stack[-2]=='(' and stack[-1]==')':
            stack.pop()
            stack.pop()
    return True if len(stack)==0 else False

def solution(s): #test5,test11 error. it has a counterexample, ())()())
    return True if s.count('(')==s.count(')') and s[0]=='(' and s[-1]==')' else False

def solution(s): #1st
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0