def solution(numbers, hand):
    cur = ['*', '#']

    answer = ''

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            cur[0] = num
            continue

        if num in [3, 6, 9]:
            answer += 'R'
            cur[1] = num
            continue

        if num in [2, 5, 8, 0]:
            left_hand = how_long(cur[0], num)
            right_hand = how_long(cur[1], num)
            if left_hand == right_hand:
                if hand == 'left':
                    answer += 'L'
                    cur[0] = num
                    continue
                else:
                    answer += 'R'
                    cur[1] = num
                    continue
            elif left_hand < right_hand:
                answer += 'L'
                cur[0] = num
                continue
            else:
                answer += 'R'
                cur[1] = num
                continue

    return answer


def how_long(s, g):

    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]

    s_ij = []

    # 좌표 찾기
    for i in range(4):
        if len(s_ij) == 2:
            break
        for j in range(3):
            if len(s_ij) == 2:
                break
            if phone[i][j] == s:
                s_ij.append(i)
                s_ij.append(j)
    ans = 0
    while s != g:
        if s in [1, 4, 7, '*']:
            s = phone[s_ij[0]][s_ij[1] + 1]
            s_ij = [s_ij[0], s_ij[1] + 1]
            ans += 1
            continue

        elif s in [3, 6, 9, '#']:
            s = phone[s_ij[0]][s_ij[1] - 1]
            s_ij = [s_ij[0], s_ij[1] - 1]
            ans += 1
            continue

        if g == 0:
            while s != 0:
                s = phone[s_ij[0]+1][s_ij[1]]
                s_ij = [s_ij[0]+1, s_ij[1]]
                ans += 1
            return ans

        if s == 0:
            while s != g:
                s = phone[s_ij[0] - 1][s_ij[1]]
                s_ij = [s_ij[0] - 1, s_ij[1]]
                ans += 1
            return ans

        if s > g:
            s = phone[s_ij[0] - 1][s_ij[1]]
            s_ij = [s_ij[0] - 1, s_ij[1]]
            ans += 1
            continue
        else:
            s = phone[s_ij[0] + 1][s_ij[1]]
            s_ij = [s_ij[0] + 1, s_ij[1]]
            ans += 1
            continue

    return ans