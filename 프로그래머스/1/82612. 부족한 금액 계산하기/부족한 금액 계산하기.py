def solution(price, money, count):
    answer = 0
    total_count = 0
    for i in range(count+1):
        total_count += i
    total_price = total_count * price
    if total_price > money:
        answer = total_price - money
    return answer