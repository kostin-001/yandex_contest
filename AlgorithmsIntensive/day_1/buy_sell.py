"""
The main idea here is to compare two relations: best buy price (min_idx), and best sell price (max_idx), vs current buy price (current_min) and current sell price (i).
Having this, we can compare max_idx/min_idx vs i/current_min and if second relation is greater, than "i" becomes new best sell price and current_min becomes new best buy price.
For convince the formula was changed to max_idx * current_min and min_idx * i.
"""


def calc_days(arr):
    if len(set(arr)) == 1:
        return 0, 0
    min_idx = 0
    max_idx = 0
    current_min = 0
    for i in range(1, len(arr)):
        if arr[max_idx] * arr[current_min] < arr[min_idx] * arr[i]:  # updating best buy and best sell
            min_idx = current_min
            max_idx = i
        if arr[i] < arr[current_min]:  # updating current min
            current_min = i
    min_idx += 1
    max_idx += 1
    if min_idx == max_idx:
        min_idx = max_idx = 0
    return min_idx, max_idx


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    print(*calc_days(nums))
