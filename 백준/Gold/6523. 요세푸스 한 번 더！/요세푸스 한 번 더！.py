while True:
    try:
        N, a, b = list(map(int, input().split()))
    except:
        break
    pure = N
    chance = {}
    check = False
    cur_drink = 0
    while not check:
        next_drink = (((cur_drink%N) * (cur_drink%N) * (a%N))+ (b % N)) % N
        if chance.get(next_drink) is None:
            chance[next_drink] = 1
        elif chance.get(next_drink) == 2:
            break
        else:
            chance[next_drink] = 2
        cur_drink = next_drink
    for num in chance.values():
        if num > 1:
            pure -= 1
    print(pure)