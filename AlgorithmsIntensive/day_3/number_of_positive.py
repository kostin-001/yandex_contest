"""
Main idea here is to use prefix sum (like a counter of positive nums in a sequence).
"""


def count_positive(num_seq: list[int], n: int, s) -> str:
    ans = []
    prefix = [0] * n
    for i, x in enumerate(num_seq):
        if x > 0:
            prefix[i] = prefix[i - 1] + 1
        else:
            prefix[i] = prefix[i - 1]
    prefix.insert(0, 0)
    for c in s:
        ans.append(str(prefix[c[1]] - prefix[c[0] - 1]))
    return "\n".join(ans)


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    num_of_q = int(input())
    coords = []
    for _ in range(num_of_q):
        a, b = map(int, input().split())
        coords.append((a, b))
    print(count_positive(nums, n, coords))
