dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(1, 11):
    test_case = int(input())
    ladder_map = [list(map(int, input().split())) for i in range(100)]
    answer = 0

    for x in range(100):
        cur_x = x
        cur_y = 0

        if ladder_map[cur_y][cur_x] == 1:
            cur_y += 1

            while cur_y != 99:
                for i in range(2):
                    flag = False

                    while 0 <= cur_x + dx[i] < 100 and ladder_map[cur_y][cur_x + dx[i]] == 1:
                        flag = True
                        cur_x += dx[i]
                    if flag:
                        break
                cur_y += 1
        if ladder_map[cur_y][cur_x] == 2:
            answer = x
            break
    print(f'#{test_case} {answer}')