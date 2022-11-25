"""
The main idea here is to find in th first half of the palindrome first letter, different from "a" and replace it with "a".
If all letters are "a", then replace last letter with "b".
Otherwise, palindrome len = 1
"""


def break_palindrome(palindrome: str) -> str:
    if len(palindrome) == 1:
        return ""
    result = list(palindrome)
    flag = False
    for i in range(len(result) // 2):
        if result[i] != 'a':
            result[i] = 'a'
            flag = True
            break
    if flag:
        return "".join(result)
    else:
        result[-1] = 'b'
        return "".join(result)


if __name__ == '__main__':
    p = input()
    print(break_palindrome(p))
