T = int(input())
for test_case in range(1, T+1):
    input_list = list(map(int, input().split()))
    N = input_list[0]
    X = input_list[1]
    map_data = [[0]*N for _ in range(N)]
    fail_count = 0

    for i in range(N):
        map_data[i] = list(map(int, input().split()))

    for i in range(N):
        cur_pos = map_data[i][0]
        stack = 0
        cur_length = 1
        for j in range(1, N):
            if cur_pos != map_data[i][j]:
                if cur_length < 0:
                    fail_count += 1
                    break
                if cur_pos < map_data[i][j]:
                    if cur_length >= (map_data[i][j] - cur_pos) * X:
                        cur_length = 1
                        cur_pos = map_data[i][j]
                    else:
                        fail_count += 1
                        break
                else:
                    stack = (cur_pos - map_data[i][j]) * X
                    cur_pos = map_data[i][j]
                    cur_length = 1 - stack
            else:
                cur_length += 1
            if j == N-1 and cur_length < 0:
                fail_count += 1
                break

    for i in range(N):
        cur_pos = map_data[0][i]
        stack = 0
        cur_length = 1
        for j in range(1, N):
            if cur_pos != map_data[j][i]:
                if cur_length < 0:
                    fail_count += 1
                    break
                if cur_pos < map_data[j][i]:
                    if cur_length >= (map_data[j][i] - cur_pos) * X:
                        cur_length = 1
                        cur_pos = map_data[j][i]
                    else:
                        fail_count += 1
                        break
                else:
                    stack = (cur_pos - map_data[j][i]) * X
                    cur_pos = map_data[j][i]
                    cur_length = 1 - stack
            else:
                cur_length += 1
            if j == N-1 and cur_length < 0:
                fail_count += 1
                break

    print(f'#{test_case} {N*2-fail_count}')
