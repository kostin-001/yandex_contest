def get_width(table_length: int, s_coords: list[(int, int)]) -> list[int]:
    widths = [0] * (table_length + 1)
    for c in s_coords:
        widths[c[0] - 1] += 1  # since numeration in task starts from 1
        widths[c[1]] -= 1
    curr = 0
    for i in range(len(widths)):  # creating list of sums
        widths[i] = curr + widths[i]
        curr = widths[i]
    return widths


if __name__ == '__main__':
    l, n, m = map(int, input().split())
    socks_coords = []
    for _ in range(n):
        a, b = map(int, input().split())
        socks_coords.append((a, b))
    width = get_width(l, socks_coords)
    for _ in range(m):
        print(width[int(input()) - 1])  # since numeration in task starts from 1
