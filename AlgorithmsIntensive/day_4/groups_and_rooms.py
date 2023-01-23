def get_max_intersection(groups_list: list[int], rooms_list: list[int]) -> int:
    cnt = 0
    r_idx = 0
    for g in groups_list:  # iterate over groups
        if r_idx >= len(rooms_list):
            break
        for r_idx in range(r_idx, len(rooms_list)):   # iterate over remaining rooms
            if g <= rooms_list[r_idx]:  # if room big enough
                cnt += 1
                r_idx += 1
                break
    return cnt


if __name__ == '__main__':
    n = int(input())
    n_nums = sorted(map(int, input().split()))
    m = int(input())
    m_nums = sorted(map(int, input().split()))
    print(get_max_intersection(n_nums, m_nums))
