def bfs(start):
    visited = [0] * 101
    queue = [start]
    next_queue = []
    visited[start] = 1
    depth = 0
    max_num = 0
    while queue:
        cur_num = queue.pop()
        if max_num < cur_num:
            max_num = cur_num
        for i in range(1, 101):
            if visited[i]:
                continue
            if board[cur_num][i] == 0:
                continue
            visited[i] = 1
            next_queue.append(i)
        if not queue:
            if not next_queue:
                return max_num
            max_num = 0
            queue.extend(next_queue)
            next_queue = []
            depth += 1
    print(depth)


for test_case in range(1, 11):
    length, start = list(map(int, input().split()))
    board = [[0] * 101 for _ in range(101)]
    phone = list(map(int, input().split()))
    for i in range(length//2):
        board[phone[i*2]][phone[i*2+1]] = 1
    answer = bfs(start)
    print(f'#{test_case} {answer}')
