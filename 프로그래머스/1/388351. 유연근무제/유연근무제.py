def solution(schedules, timelogs, startday):
    answer = 0
    n = len(timelogs)
    answer = n
    for i in range(n):
        hour = schedules[i] // 100
        minute = schedules[i] % 100
        total_minute = hour * 60 + minute
        for j in range(7):
            if (startday + j) % 7 == 6 or (startday + j) % 7 == 0:
                continue
            cur_hour = timelogs[i][j] // 100
            cur_minute = timelogs[i][j] % 100
            cur_total_minute = cur_hour * 60 + cur_minute
            if cur_total_minute > total_minute + 10:
                answer -= 1
                break
    return answer