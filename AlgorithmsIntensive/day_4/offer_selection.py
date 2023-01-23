def get_max_lectures(intervals: list[(int, int)]) -> int:
    cnt = 0
    t = -1
    for i in intervals:
        if i[0] >= t:
            t = i[1]
            cnt += 1
    return cnt


if __name__ == '__main__':
    n = int(input())
    time_intervals = []
    for _ in range(n):
        a, b = map(int, input().split())
        time_intervals.append((a, b))
    time_intervals.sort(key=lambda x: x[1])  # sort by end time
    print(get_max_lectures(time_intervals))
