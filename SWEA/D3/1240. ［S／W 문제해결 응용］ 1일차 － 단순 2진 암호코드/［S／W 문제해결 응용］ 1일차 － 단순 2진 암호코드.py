def check(data):
    if bin_dict.get(data) is not None:
        return bin_dict.get(data)
    else:
        return 0


def check_valid(string):
    sum_data = 0
    if len(string) < 8:
        return 0
    for i in range(8):
        if (i+1) % 2 == 1:
            sum_data += int(string[i]) * 3
        else:
            sum_data += int(string[i])
    if sum_data % 10 == 0:
        return 1
    else:
        return 0


def sum_string(string):
    sum_char = 0
    for i in range(8):
        sum_char += int(string[i])
    return sum_char


T = int(input())
for test_case in range(1, T+1):
    bin_dict = {'0001101' : '0', '0011001' : '1', '0010011' : '2', '0111101' : '3', '0100011' : '4',
                '0110001' : '5', '0101111' : '6', '0111011' : '7', '0110111' : '8', '0001011' : '9'}
    N, M = list(map(int, input().split()))
    answer = ''
    for i in range(N):
        temp = input()
        if '1' in temp:
            board = temp
    for i in range(M-56-1):
        if check(board[i:i+7]):
            string = bin_dict.get(board[i:i+7])
            for j in range(1, 8):
                if not check(board[i+7*j:i+7+7*j]):
                    break
                else:
                    string += check(board[i+7*j:i+7+7*j])
            else:
                if check_valid(string):
                    answer = sum_string(string)
                    break
        else:
            continue
    if not answer:
        answer = 0
    print(f'#{test_case} {answer}')
