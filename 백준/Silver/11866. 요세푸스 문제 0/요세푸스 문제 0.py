from collections import deque

N, K = list(map(int, input().split()))
q = deque()
answer = '<'
for i in range(N):
    q.append(i+1)
while len(q) > 1:
    for i in range(K-1):
        q.rotate(-1)
    answer += (str(q.popleft())) + ', '
answer += (str(q.popleft())) + '>'
print(answer)