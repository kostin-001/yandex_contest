def create_mapping(items: list[int], n: int) -> tuple[list[int], int]:
    """
    :param items: initial list of numbers
    :param n: number of numbers in list
    :return:
       - list where each positive number represent len of even subsequence and each negative number represent len of odd subsequence
       - len of longest even sequence
    """
    maps = []
    cnt = 0
    max_even = 0
    for i in range(n):
        if items[i] % 2 == 1:
            if cnt > 0:
                max_even += cnt
                maps.append(cnt)
                cnt = -1
            else:
                cnt -= 1
        else:
            if cnt < 0:
                maps.append(cnt)
                cnt = 1
            else:
                cnt += 1
    if cnt > 0:
        max_even += cnt
        maps.append(cnt)
    if maps[0] < 0:  # we don't care about first odd numbers
        maps.pop(0)
    return maps, max_even


def find_nice_list(items: list[int], k: int, n: int) -> int:
    """
    :param items: initial list of numbers
    :param k: number of available replacements
    :param n: number of numbers in list
    :return: len of max sequence of even numbers for given number of replacements
    """
    maps, max_available_moves = create_mapping(items, n)
    available_moves = max_available_moves  # available_moves is remaining number of available even numbers
    remaining_k = k  # remaining_k is remaining number of replacements
    seq_len = 0  # current sequence len
    max_len = 0  # max sequence len
    l = 0  # pointer to the left part of the window
    for r in range(len(maps)):  # r is a pointer to the right part of the window
        el = maps[r]
        if el > 0:  # if next sequence is a sequence of even numbers
            if available_moves >= el:  # if this sequence  was not used
                seq_len += el
                max_len = max(max_len, seq_len)
                available_moves -= el
            else:
                max_len = max(max_len, seq_len + available_moves)
                break

        else:  # if next sequence is a sequence of odd numbers
            el = abs(el)
            if remaining_k >= el:  # if remaining number of replacements is enough to move
                seq_len += el
                max_len = max(max_len, seq_len)
                available_moves -= el
                remaining_k -= el
                continue
            else:  # if remaining number of replacements is not enough to move
                max_len = max(max_len, seq_len + remaining_k)
                while l < r:  # move left window pointer
                    temp_el = maps[l]
                    if temp_el > 0:  # breaking link with previous even numbers
                        available_moves += temp_el
                        seq_len -= temp_el
                        l += 1
                    else:
                        temp_el = abs(temp_el)
                        if temp_el >= el or temp_el + remaining_k >= el:  # move with step = 1 for odd numbers to keep window as far to the left as possible
                            maps[l] = -(temp_el + remaining_k - el)
                            seq_len += remaining_k
                            remaining_k = 0
                            max_len = max(max_len, seq_len)
                            break
                        else:  # if len of odd sequence is not enough big
                            seq_len -= temp_el
                            remaining_k += temp_el
                            available_moves += temp_el
                            l += 1
                if l == r:  # if there is a big gap of odd numbers
                    step = max(el + maps[l], k)
                    maps[l] = -step
                    available_moves = max_available_moves - step
                    remaining_k = k - step
                    seq_len = step
                    max_len = max(max_len, seq_len)

    return min(max_len, max_available_moves)


if __name__ == '__main__':
    number_of_elements, number_of_available_replacement = map(int, input().split())
    nums = list(map(int, input().split()))

    print(find_nice_list(nums, number_of_available_replacement, number_of_elements))
