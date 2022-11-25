"""Euler diagrams here can help"""

if __name__ == '__main__':
    _ = input()
    a = set(map(int, input().split()))
    _ = input()
    b = set(map(int, input().split()))
    _ = input()
    c = set(map(int, input().split()))

    ab = a.intersection(b)
    union_ab = a.union(b)
    res = ab.union(c.intersection(union_ab))
    print(*sorted(res))
