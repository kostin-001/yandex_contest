from collections import Counter


def get_majority(lst: list) -> int:
    cnt = Counter(lst)
    return cnt.most_common(1)[0][0]


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(get_majority(nums))
