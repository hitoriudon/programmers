def solution(board, moves): #my
    answer = 0
    box = []
    for i in moves:
        for j in range (len(board)):
            if board[j][i-1] != 0:
                box.append(board[j][i-1])
                board[j][i-1] = 0
                if len(box)>=2 and box[-1]==box[-2]:
                    box.pop()
                    box.pop()
                    answer+=2
                break
    return answer


def solution(board, moves): #runtime error
    answer = 0
    box = [0]
    for i in moves:
        for j in range (len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                box.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if box[-1]==box[-2]:
            box.pop()
            box.pop()
            answer+=2
    return answer