"""
Main idea contains 2 parts:
outer loop - is to use binary search to find such minimum power of potion which will be enough to include in list of created potions (binary search in get_max_profit method) - idea similar to caws in stalls task.
inner loop - utilize two pointers to get current max power and min power items (which will be used for potion preparation) and prefix sum in order to speed up calculations.
"""


def check_limit(m, k, n, items, prefix_sum):
    res = 0
    cnt = 0
    j = 1
    while j < n - 1 and (items[0] + items[j] >= m):
        j += 1

    for i in range(n):
        if i >= j:
            break
        while j > i and items[i] + items[j] < m:
            j -= 1
        cnt += (j - i)
        res += prefix_sum[j] - prefix_sum[i] + items[i] * (j - i)

    if cnt >= k:
        return True, res - (cnt - k) * m
    else:
        return False, 0


def get_max_profit(items, k, n):
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + items[i - 1]
    prefix_sum = prefix_sum[1:]

    r = max(items[0] * 2, abs(items[-1] * 2))
    l = -r
    while r > l:
        m = (l + r + 1) // 2
        res = check_limit(m, k, n, items, prefix_sum)
        if res[0]:
            l = m
        else:
            r = m - 1
    return check_limit(l, k, n, items, prefix_sum)[1]


if __name__ == '__main__':
    n, k = map(int, input().split())
    n += 1
    profit = f"0 {input()}"
    profit = sorted(map(int, profit.split()), reverse=True)
    print(f"{get_max_profit(profit, k, n)}")
