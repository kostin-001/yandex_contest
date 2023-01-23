"""
This task can be solved with different approaches, for example with usage of trees.
Approach used in this code less memory effective, since it stores whole path for the file, and this is the reason of higher memory consumption.
However, this approach can give constant speed (of query execution) if we will have small tree and a lot of queries.
"""


def get_file_paths(nodes: list[str]) -> dict:
    path = []
    full_paths = {}
    for node in nodes:
        curr = node.strip()
        s = len(node) - len(node.lstrip())
        path = path[:s]
        path.append(curr)
        if curr not in full_paths:
            full_paths[curr] = "/" + "/".join(path)

    return full_paths


if __name__ == '__main__':
    fn = input()
    n = int(input())
    files_and_folders = []
    for _ in range(n):
        files_and_folders.append(input())
    paths = get_file_paths(files_and_folders)
    print(paths[fn])
