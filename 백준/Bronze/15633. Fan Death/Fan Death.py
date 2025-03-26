n = int(input())

mini_n = int(n ** (1/2))
total = []
for i in range(1, mini_n+1):
    if n % i == 0:
        total.append(i)
        if i < n // i:
            total.append(n//i)
total_ans = sum(total)
total_ans *= 5
print(total_ans - 24)