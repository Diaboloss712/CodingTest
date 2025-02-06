T = int(input())
for test_case in range(1, T + 1):
    input_list = input().split()
    num_list = [0] * 10
    count = 0
    for num in input_list[0]:
        num_list[int(num)] += 1

    for i in range(10):
        while num_list[i] >= 3:
            num_list[i] -= 3
            count += 1

    for i in range(8):
        while num_list[i] >= 1:
            if num_list[i + 1] >= 1 and num_list[i + 2] >= 1:
                num_list[i] -= 1
                num_list[i + 1] -= 1
                num_list[i + 2] -= 1
                count += 1
            else:
                break
    if count == 2:
        print(f'#{test_case} true')
    else:
        print(f'#{test_case} false')