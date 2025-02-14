def left_magnet(magnet_num, direction):
    if magnet_num - 1 < 0:
        return
    else:
        if Magnet[magnet_num - 1][(2 + Arrow[magnet_num-1]) % 8] != Magnet[magnet_num][(6 + Arrow[magnet_num]) % 8]:
            left_magnet(magnet_num-1, -direction)
            Arrow[magnet_num - 1] += direction
 
 
def right_magnet(magnet_num, direction):
    if magnet_num + 1 > 3:
        return
    else:
        if Magnet[magnet_num + 1][(6 + Arrow[magnet_num + 1]) % 8] != Magnet[magnet_num][(2 + Arrow[magnet_num]) % 8]:
            right_magnet(magnet_num+1, -direction)
            Arrow[magnet_num + 1] += direction
 
 
T = int(input())
for test_case in range(1, T+1):
    K = int(input())
    answer = 0
    Magnet = [[0] * 8 for _ in range(4)]
    Rotate = [[0] * 2 for _ in range(K)]
    Arrow = [24, 24, 24, 24]
    for i in range(4):
        Magnet[i] = list(map(int, input().split()))
    for i in range(K):
        Rotate[i] = list(map(int, input().split()))
    for i in range(K):
        left_magnet(Rotate[i][0]-1, Rotate[i][1])
        right_magnet(Rotate[i][0]-1, Rotate[i][1])
        Arrow[Rotate[i][0]-1] -= Rotate[i][1]
    for j in range(4):
        if Magnet[j][Arrow[j] % 8] == 1:
            answer += 2 ** j
    print(f'#{test_case} {answer}')