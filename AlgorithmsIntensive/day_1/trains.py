def convert_to_minutes(timestamp_list):
    """
        simple function to convert list of strings HH:MM to list of int (minutes)
    :param timestamp_list: list of strings HH:MM
    :return: list of int (minutes)
    """
    res = []
    for t in timestamp_list:
        h, m = map(int, t.split(":"))
        res.append(h * 60 + m)
    res.sort()
    return res


def calc_days(minutes):
    diff = 24 * 60 + minutes[0] - minutes[-1]  # corner case for last train on this day and first train on next day like 23:59 and 00:01
    for i in range(1, len(minutes)):
        diff = min(diff, minutes[i] - minutes[i - 1])  # this is possible since minutes list is sorted
    return diff


if __name__ == '__main__':
    n = int(input())
    times = input().split()
    print(calc_days(convert_to_minutes(times)))
