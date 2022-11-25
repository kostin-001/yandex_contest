import re


def get_profit(expected: list, received: list) -> str:
    original_expectation = set()
    lowercase_expectation = {}
    lowercase_no_vowels_expectation = {}
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
        if r in original_expectation:
            ans.append(r)
        elif r.lower() in lowercase_expectation:
            ans.append(lowercase_expectation[r.lower()])
        else:
            r = re.sub(r"[aeiou]", "0", r.lower())
            if r in lowercase_no_vowels_expectation:
                ans.append(lowercase_no_vowels_expectation[r])
            else:
                ans.append("")
    return " ".join(ans)


_ = int(input())
expected = input().split()
_ = int(input())
received = input().split()
print(get_profit(expected, received))
