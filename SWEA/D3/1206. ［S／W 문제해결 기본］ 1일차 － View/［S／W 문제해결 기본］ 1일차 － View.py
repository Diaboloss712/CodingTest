for test_case in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))
    building_count = 0
    for i in range(2, N-2):
        if height[i] > height[i+1] and height[i] > height[i+2] and height[i] > height[i-1] and height[i] > height[i-2]:
            building_count += height[i] - max(height[i-2], height[i-1], height[i+1], height[i+2])
    print(f'#{test_case} {building_count}')