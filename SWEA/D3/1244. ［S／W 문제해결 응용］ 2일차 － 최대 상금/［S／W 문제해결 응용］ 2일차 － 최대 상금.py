import heapq


def exchange(start, board, chance, duplicate):
    temp = []
    temp_index = []
    previous_num = 0
    while chance != change_num:
        if start >= len(board):  # 남은 교환 처리
            break
        max_num = int(board[start])
        max_index = start

        for i in range(start + 1, len(board)):  # 현재보다 큰값 찾기
            if max_num <= int(board[i]):
                max_num = int(board[i])
                max_index = i
        if max_num > int(board[start]):
            if previous_num == max_num or not temp:
                heapq.heappush(temp, -(int(board[start])))
                heapq.heappush(temp_index, max_index)
                previous_num = max_num
            else:
                previous_num = max_num
                while temp:
                    board[heapq.heappop(temp_index)] = str(-heapq.heappop(temp))
                heapq.heappush(temp, -(int(board[start])))
                heapq.heappush(temp_index, max_index)
            (board[max_index]), (board[start]) = (board[start]), (board[max_index])
            chance += 1
        start += 1
    while temp:
        board[heapq.heappop(temp_index)] = str(-heapq.heappop(temp))
    if chance != change_num:
        if duplicate:
            return board
        elif (chance - change_num) % 2 == 1:
            board[len(board) - 1], board[len(board) - 2] = board[len(board) - 2], board[len(board) - 1]
            return board
        else:
            return board
    return board


def dup_check(num_board):
    dup_list = []
    while num_board > 10:
        dup_list.append(num_board % 10)
        num_board //= 10
    dup_list.append(num_board)
    dup_list.sort()
    for i in range(len(dup_list) - 1):
        if dup_list[i] == dup_list[i + 1]:
            return True
        else:
            continue
    return False


T = int(input())
for test_case in range(1, T + 1):
    number_board, change_num = list(map(int, input().split()))
    dup = dup_check(number_board)
    answer = exchange(0, list(str(number_board)), 0, dup)
    print(f'#{test_case}', end=" ")
    for num in answer:
        print(num, end="")
    print()
