import re


def get_profit(expected: list, received: list) -> str:
    original_expectation = set()  # first order substance
    lowercase_expectation = {}  # second order substance
    lowercase_no_vowels_expectation = {}  # third order substance
    for e in expected:
        original_expectation.add(e)
        e_lower = e.lower()
        e_lower_no_vowels = re.sub(r"[aeiou]", "0", e_lower)
        if e_lower not in lowercase_expectation:
            lowercase_expectation[e_lower] = e
        if e_lower_no_vowels not in lowercase_no_vowels_expectation:
            lowercase_no_vowels_expectation[e_lower_no_vowels] = e
    ans = []

    for r in received:
        if r in original_expectation:  # check if received substance is a first order substance
            ans.append(r)
        elif r.lower() in lowercase_expectation:  # check if received substance is a second order substance
            ans.append(lowercase_expectation[r.lower()])
        else:
            r = re.sub(r"[aeiou]", "0", r.lower())
            if r in lowercase_no_vowels_expectation:  # check if received substance is a third order substance
                ans.append(lowercase_no_vowels_expectation[r])
            else:
                ans.append("")
    return " ".join(ans)


if __name__ == '__main__':
    _ = int(input())
    exp = input().split()
    _ = int(input())
    rec = input().split()
    print(get_profit(exp, rec))
