def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    start = 0
    end = distance
    mid = (start + end) // 2
    while start <= end:
        count_over = 0
        cur_pos = 0
        mid = (start + end) // 2
        for rock in rocks:
            if mid > (rock - cur_pos):
                count_over += 1
            else:
                cur_pos = rock
        if count_over > n:
            end = mid-1
        else:
            answer = mid
            start = mid+1
    return answer