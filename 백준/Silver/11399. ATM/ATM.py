import sys

N = int(sys.stdin.readline())  # N: 사람의 수
Pi = list(map(int, sys.stdin.readline().split()))  # 돈을 인출하는데 걸리는 시간

Pi.sort()

time_sum = []

for i in range(N):
    time_sum.append(sum(Pi[0:i+1]))

print(sum(time_sum))