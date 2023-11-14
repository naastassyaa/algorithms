import heapq


def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    queue = [(0.0, start)]

    while queue:
        distance, vertex = heapq.heappop(queue)
        if visited[vertex]:
            continue
        visited[vertex] = True

        for v, w in graph[vertex]:
            if dist[vertex] + w < dist[v]:
                dist[v] = dist[vertex] + w
                heapq.heappush(queue, (dist[v], v))

    return dist


with open("gamsrv.in", "r") as input_file:
    N, M = map(int, input_file.readline().split())
    clients = [int(i) - 1 for i in input_file.readline().split()]
    graph = [[] for _ in range(N)]

    for _ in range(M):
        startnode, endnode, latency = map(int, input_file.readline().split())
        graph[startnode - 1].append([endnode - 1, latency])
        graph[endnode - 1].append([startnode - 1, latency])

min_max_latency = float('inf')
min_node = -1

for server_node in range(N):
    if server_node not in clients:
        max_latency = 0
        dist = dijkstra(graph, server_node)
        for i in range(len(dist)):
            if i in clients and dist[i] > max_latency:
                max_latency = dist[i]

        if max_latency < min_max_latency:
            min_max_latency = max_latency
            min_node = server_node

with open("gamsrv.out", "w") as output_file:
    output_file.write(str(min_max_latency) + " ")
    output_file.write(str(min_node + 1))


