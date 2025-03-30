import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
distance = [INF] * (V + 1)
board = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    board[u].append((w, v))

def dijkstra(start_num):
    q = []
    heapq.heappush(q, (0, start_num))
    distance[start_num] = 0
    while q:
        cost, cur_node = heapq.heappop(q)
        if distance[cur_node] < cost:
            continue
        for next_cost, next_node in board[cur_node]:
            next_distance = cost + next_cost
            if distance[next_node] > next_distance:
                distance[next_node] = next_distance
                heapq.heappush(q, (next_distance, next_node))

dijkstra(K)
for i in range(1, V + 1):
    print('INF' if distance[i] == INF else distance[i])
