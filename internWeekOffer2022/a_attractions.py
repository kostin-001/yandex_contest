def get_overlap(a1, a2):
    short_len = min(len(a1), len(a2))
    overlap12 = -1
    overlap21 = -1
    for i in range(1, short_len + 1):
        if a1[-i:] == a2[:i]:
            overlap12 = i
        if a2[-i:] == a1[:i]:
            overlap21 = i
    return overlap12, overlap21


def merge(a1, a2, idx):
    if idx >= 0:
        a1 = a1[:-idx]
    return a1 + a2


def get_shortest_path(cities):
    while len(cities) > 1:
        max_overlap = -1
        ci1 = cities[0]
        ci2 = cities[1]
        for i in range(len(cities) - 1):
            c1 = cities[i]
            c2 = cities[i + 1]

            o1, o2 = get_overlap(c1, c2)
            if max(o1, o2) > max_overlap:
                max_overlap = max(o1, o2)
                ci1, ci2 = c1, c2
                if o2 > o1:
                    ci2, ci1 = c1, c2

        cities.remove(ci1)
        cities.remove(ci2)
        cities.append(merge(ci1, ci2, max_overlap))

    cities = cities[0]
    return cities


if __name__ == '__main__':
    cities = []
    cities_words = set()
    for _ in range(3):
        _, b = input().split(maxsplit=1)
        if b not in cities_words:
            cities_words.add(b)
            b = list(map(int, b.split()))
            cities.append(b)

    result = get_shortest_path(cities)
    print(len(result))
    print(" ".join(map(str, result)))
