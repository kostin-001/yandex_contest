def calc_repetition(v, step):
    window = set()
    for i in range(len(v)):
        if v[i] in window:
            return "YES"
        window.add(v[i])
        if i >= k:
            window.remove(v[i - k])
    return "NO"


n, k = map(int, input().split())
values = list(map(int, input().split()))

print(calc_repetition(values, k))
