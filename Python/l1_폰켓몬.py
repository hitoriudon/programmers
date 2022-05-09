def solution(nums): #my
    N = len(nums)
    return N/2 if len(list(set(nums)))>N/2 else len(list(set(nums)))