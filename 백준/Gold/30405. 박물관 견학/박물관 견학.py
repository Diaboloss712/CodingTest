N, M = list(map(int, input().split()))
gate = []
for i in range(N):
    line = list(map(int, input().split()))
    gate.append(line[1])
    gate.append(line[len(line)-1])
gate.sort()
print(gate[N-1])