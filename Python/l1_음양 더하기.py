def solution(absolutes, signs): #my
    total = 0
    for n, s in zip(absolutes, signs):
        total += n*(-1) if s==False else n
    return total

def solution(absolutes, signs): #1st ... 이걸 하고 싶었는데
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))