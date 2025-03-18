def check():
    global answer
    for i in range(1 << N):
        arr = []
        for j in range(N):
            if i & (1 << j):
                arr.append(height[j])
        if sum(arr) >= B:
            if answer >= sum(arr):
                answer = sum(arr)


T = int(input())
for test_case in range(1, T+1):
    answer = 1e9
    N, B = list(map(int, input().split()))
    height = list(map(int, input().split()))
    length = len(height)
    check()
    print(f'#{test_case} {answer - B}')
