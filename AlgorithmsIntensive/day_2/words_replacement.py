"""
Brute force
"""


def simplify_text(vocab: set, words: list) -> str:
    ans = []
    for w in words:
        for j in range(1, len(w)):
            if w[:j] in vocab:
                ans.append(w[:j])
                break
        else:
            ans.append(w)
    return " ".join(ans)


if __name__ == '__main__':
    v = set(input().split())
    w = input().split()
    print(simplify_text(v, w))
