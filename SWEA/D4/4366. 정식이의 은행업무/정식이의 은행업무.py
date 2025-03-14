def check(num):
    div_check = abs(int(num, 2) - int(tri_num, 3))
    while div_check > 3:
        if div_check % 3 != 0:
            return 0
        div_check //= 3
    return 1


T = int(input())
for test_case in range(1, T+1):
    answer = 0
    bin_num = input()
    tri_num = input()

    for i in range(len(bin_num)):
        check_num = bin_num
        if check_num[i] == '1':
            t_num = check_num[:i] + '0' + check_num[i + 1:]
            if check(t_num):
                answer = int(t_num, 2)
                break
        else:
            t_num = check_num[:i] + '1' + check_num[i + 1:]
            if check(t_num):
                answer = int(t_num, 2)
                break
    print(f'#{test_case} {answer}')