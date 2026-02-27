def solution(n, q, ans):
    def count_bits(x):
        cnt = 0
        while x:
            x &= x - 1
            cnt += 1
        return cnt

    m = len(q[0])

    check = []
    for nums in q:
        bit = 0
        for num in nums:
            bit |= 1 << (num - 1)
        check.append(bit)

    answer = 0

    mask = (1 << m) - 1
    limit = 1 << n

    while mask < limit:

        for bit, a in zip(check, ans):
            if count_bits(mask & bit) != a:
                break
        else:
            answer += 1

        c = mask & -mask
        r = mask + c
        mask = (((r ^ mask) >> 2) // c) | r

    return answer