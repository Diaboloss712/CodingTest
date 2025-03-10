from collections import deque

T = int(input())
for test_case in range(1, T+1):
    N, T = list(map(int, input().split()))
    deck = deque([])
    first_deck = deque([])
    second_deck = deque([])
    for i in range(N, 0, -1):
        deck.appendleft(i)
    for _ in range(T):
        deck.rotate(N*37//100)
        for i in range(N - N//2):
            first_deck.append(deck.popleft())
        while deck:
            second_deck.append(deck.popleft())
        for i in range(1, N+1):
            if i % 2 == 1:
                deck.append(first_deck.popleft())
            else:
                deck.append(second_deck.popleft())
    print(f'#{test_case}',end=" ")
    while deck:
        print(deck.popleft(), end=" ")
    print()