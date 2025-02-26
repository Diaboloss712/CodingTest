def solution(numbers, hand):
    dict = {1:[0,0], 2:[0,1], 3:[0,2],
           4:[1,0], 5:[1,1], 6:[1,2],
           7:[2,0], 8:[2,1], 9:[2,2], 0:[3,1]}
    
    answer = ''
    l_pos = [3,0]
    r_pos = [3,2]
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            l_pos = dict[num]
            answer += 'L'
            continue
        if num == 3 or num == 6 or num == 9:
            r_pos = dict[num]
            answer += 'R'
            continue
        input_x = dict[num][1]
        input_y = dict[num][0]
        l_dis = abs(dict[num][0] - l_pos[0])\
                + abs(dict[num][1] - l_pos[1])
        r_dis = abs(dict[num][0] - r_pos[0])\
                + abs(dict[num][1] - r_pos[1])
        if l_dis > r_dis:
            r_pos = dict[num]
            answer += 'R'
        elif l_dis == r_dis:
            if hand == "left":
                l_pos = dict[num]
                answer += 'L'
            else:
                r_pos = dict[num]
                answer += 'R'
        else:
            l_pos = dict[num]
            answer += 'L'
                
    return answer