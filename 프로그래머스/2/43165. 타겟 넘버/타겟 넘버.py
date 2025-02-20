def solution(numbers, target):
    global answer
    answer = 0
    visited = [0] * len(numbers)
    dfs(numbers, target, 0, 0, visited)
    return answer

def dfs(numbers, target, depth, cur_sum, visited):
    global answer
    if depth == len(numbers):
        if cur_sum == target:
            answer += 1
        return
    else:
        for i in range(2):
            numbers[depth] = numbers[depth] * (-1) ** i
            visited[depth] = 1
            dfs(numbers, target, depth+1, numbers[depth] + cur_sum, visited)
            visited[depth] = 0