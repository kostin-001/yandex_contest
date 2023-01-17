"""
Main idea contains 2 parts:
outer loop - is to use binary search to find such maximum distance which will be enough to place k cows in stalls (binary search in get_max_profit method).
inner loop - just simple caw counter.
"""


def count_cows(m, k, n, coords):
    cnt = 1
    prev = coords[0]
    for i in range(1, n):
        if coords[i] - prev >= m:
            prev = coords[i]
            cnt += 1
    return cnt >= k


def get_max_distance(stall_coords, k, n):
    l = 0
    r = stall_coords[-1]
    while r > l:
        m = (l + r + 1) // 2
        if count_cows(m, k, n, stall_coords):
            l = m
        else:
            r = m - 1
    return l


if __name__ == '__main__':
    n, k = map(int, input().split())
    stalls_coords = list(map(int, input().split()))
    print(f"{get_max_distance(stalls_coords, k, n)}")
