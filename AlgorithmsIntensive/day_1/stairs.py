"""
Main idea here is that we utilize arithmetic progression formula here,
in particular we use sum of n first elements: s_n = (2*a_1 + d * n-1) * n / 2
From this formula we know s_n, a_1 and d, the only thing we need to find is n.
Having this we, transform formula to the quadratic equation (where we need to find x), solve it and round down the result.
"""


def get_number_of_steps(blocks):
    d = 1 + 8 * blocks
    return int(((d ** 0.5) - 1) * 0.5)


if __name__ == '__main__':
    n = int(input())
    print(get_number_of_steps(n))
