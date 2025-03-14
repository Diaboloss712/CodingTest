T = int(input())


def check():
    global answer
    for i in range(1, len(carrot_stock) - 1):
        for j in range(i + 1, len(carrot_stock)):
            a = sum(carrot_stock[:i])
            b = sum(carrot_stock[i:j])
            c = sum(carrot_stock[j:])
            if a > N // 2 or b > N // 2 or c > N // 2:
                continue
            if a == 0 or b == 0 or c == 0:
                continue
            if answer > max(a, b, c) - min(a, b, c):
                answer = max(a, b, c) - min(a, b, c)


for test_case in range(1, T + 1):
    N = int(input())
    answer = 1000
    flag = False
    size_dict = {}
    carrot_size = list(map(int, input().split()))
    carrot_size.sort()
    carrot_stock = []
    for carrot in carrot_size:
        if size_dict.get(carrot) is None:
            size_dict[carrot] = 1
        else:
            size_dict[carrot] += 1
    for key, value in enumerate(size_dict.items()):
        carrot_stock.append(value[1])

    check()
    if answer == 1000:
        answer = -1
    print(f'#{test_case} {answer}')
