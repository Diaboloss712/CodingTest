def solution(data, ext, val_ext, sort_by):
    answer = []
    data_type = {
        "code" : 0,
        "date" : 1,
        "maximum" : 2,
        "remain" : 3
        }
    for i in data:
        if i[data_type[ext]] < val_ext:
            answer.append(i)
            
    answer.sort(key=lambda x: x[data_type[sort_by]])
    
    return answer