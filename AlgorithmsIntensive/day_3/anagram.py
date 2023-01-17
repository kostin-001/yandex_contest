from collections import Counter

if __name__ == '__main__':
    a = Counter(input())  # here counter instead of set, because number of letters is important
    b = Counter(input())
    if not a - b:
        print("YES")
    else:
        print("NO")
