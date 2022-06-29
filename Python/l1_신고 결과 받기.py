def solution(id_list, report, k): #my
    id_dict = {}
    answer_dict = {}
    for name in id_list: 
        id_dict[name] = []
        answer_dict[name] = 0
    report = list(set(report))
    for i in range (len(report)):
        give , given = report[i].split()
        id_dict[given].append(give)
    for id in id_dict:
        if len(id_dict[id]) >= k:
            for name in id_dict[id]:
                answer_dict[name] += 1
    return list(answer_dict.values())