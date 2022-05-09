def solution(n): #my solution
    lst = list(map(int, str(n)))
    return sum(lst)

def sum_digit(number): #1st solution : recursive function
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 