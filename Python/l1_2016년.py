def solution(a, b): #my
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"] #1/1/16 -> FRI. So day[1] is friday.
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day[(sum(month[:a-1])+b)%7]