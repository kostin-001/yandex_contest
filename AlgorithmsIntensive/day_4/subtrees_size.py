"""
Here we utilize graph method  DFS (Depth-first search) for tree traversing in order to get size of each subtree in tree.
"""
import sys

sys.setrecursionlimit(100000)


def dfs(current, am, subtrees_size) -> int:
    subtrees_size[current] = 1
    for i in am[current]:
        if subtrees_size[i] == -1:
            subtrees_size[current] += dfs(i, am, subtrees_size)
    return subtrees_size[current]


if __name__ == '__main__':
    n = int(input())
    adjacency_matrix = []
    for i in range(n + 1):
        adjacency_matrix.append([])  # since numeration in task starts from 1

    for _ in range(n - 1):  # creating adjacency matrix
        a, b = map(int, input().split())
        adjacency_matrix[a].append(b)
        adjacency_matrix[b].append(a)
    subtree_size = [-1] * (n + 1)  # list of node sizes. -1 indicates that node was not visited (to avoid visiting already visited nodes).
    dfs(1, adjacency_matrix, subtree_size)
    print(*subtree_size[1:])
