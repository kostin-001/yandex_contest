"""
Main idea here is to use two pointers.
Other things is just math.
"""


def count_invites(age_list: list[int], number_of_people: int) -> int:
    l = 0
    r = 0
    count = 0
    for i, x in enumerate(age_list):
        while l < number_of_people and age_list[l] <= 0.5 * x + 7:
            l += 1
        while r < number_of_people and age_list[r] <= x:
            r += 1
        if r > l + 1:
            count += r - l - 1

    return count


if __name__ == '__main__':
    n = int(input())
    nums = sorted(map(int, input().split()))
    print(count_invites(nums, n))
