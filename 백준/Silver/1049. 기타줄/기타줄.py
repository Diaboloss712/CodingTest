N, M = map(int, input().split())

line_package, single_line = int(1e9), int(1e9)
for _ in range(M):
    x, y = map(int, input().split())
    if single_line > y:
        single_line = y
    if line_package > x:
        line_package = x
answer = min(single_line * N, (N // 6) * line_package + (N % 6) * single_line, ((N // 6) + 1) * line_package)
print(answer)