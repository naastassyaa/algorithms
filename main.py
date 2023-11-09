import copy
from queue import Queue


def is_valid(x, y, M, N):
    return 0 <= x < M and 0 <= y < N


def replace_adjacent_ones(matrix):
    M = len(matrix)
    N = len(matrix[0])
    matrix_copy = copy.deepcopy(matrix)

    def has_adjacent_zero(x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y, M, N) and matrix[new_x][new_y] == 0:
                    return True
        return False

    for x in range(M):
        for y in range(N):
            if matrix[x][y] == 1 and has_adjacent_zero(x, y):
                matrix_copy[x][y] = 0
    return matrix_copy



def graph_from_matrix(matrix):
    M, N = len(matrix), len(matrix[0])
    graph = {}

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                neighbors = []
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + dx, j + dy
                    if is_valid(ni, nj, M, N) and matrix[ni][nj] == 1:
                        neighbors.append((ni, nj))
                graph[(i, j)] = neighbors
    return graph


def shortest_path_graph(graph, m):
    counter = 0

    def bfs(node):
        queue = Queue()
        visited = set()
        parent_map = {}

        queue.put((node, 0))
        visited.add(node)

        while not queue.empty():
            nonlocal counter
            counter += 1
            current_node, distance = queue.get()

            if current_node[1] == m - 1:
                path = []
                while current_node:
                    path.insert(0, current_node)
                    current_node = parent_map.get(current_node)
                return distance, path

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.put((neighbor, distance + 1))
                    visited.add(neighbor)
                    parent_map[neighbor] = current_node
        return -1, []

    min_path_len = float('inf')
    min_path = []

    for node in graph:
        if node[1] == 0:
            path_len, path = bfs(node)
            if path_len != -1:
                if path_len < min_path_len:
                    min_path_len = path_len
                    min_path = path

        if min_path == m - 1:
            return min_path_len, counter, min_path

    return (min_path_len, counter, min_path) if min_path != float('inf') else (-1, counter)


with open("input.txt", "r") as f:
    matrix = []
    for line in f.readlines():
        row = [int(i) for i in line.split()]
        matrix.append(row)

matrix = replace_adjacent_ones(matrix)
graph = graph_from_matrix(matrix)
res = shortest_path_graph(graph, len(matrix[0]))

with open("output.txt", "w") as f:
    f.write(str(res))

