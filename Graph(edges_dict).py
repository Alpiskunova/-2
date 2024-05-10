def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    return graph

# Буду писать через генератор списков, множества, словарь для хранения расстояний в бфс и append, попробую использовать pop()
def read_graph_as_neigh_list():
    edge_list = read_graph_as_edges()
    graph_dict = {}
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    for v in vertex_set:
        graph_dict[v] = set()
    for edge in edge_list:
        graph_dict[edge[0]].add(edge[1])
    return graph_dict


def read_graph_as_neigh_matrix():
    edge_list = read_graph_as_edges()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)
    res_matrix = [[0] * V_num for _ in range(V_num)]
    for edge in edge_list:
        res_matrix[edge[0] - 1][edge[1] - 1] = 1
    return res_matrix


def print_matrix(matrix):
    for line in matrix:
        print(*line)


def DFS(graph, v, visited=None):
    if visited is None:
        visited = []
    print(v)
    visited.append(v)
    for neigh in graph[v]:
        if neigh not in visited:
            DFS(graph, neigh, visited)


def has_cycle(graph, v, visited=None):
    if visited is None:
        visited = []
    for neigh in graph[v]:
        if neigh in visited:
            return True
        visited.append(v)
        if has_cycle(graph, neigh, visited):
            return True
        visited.pop()
    return False


def DFS_stack(graph, v):
    stack = [v]
    visited = [v]
    while stack:
        v = stack.pop()
        print(v)
        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                stack.append(neigh)


def topologicalSort(graph):
    V_sum = len(graph)
    visited = [False] * V_sum
    stack = []
    entry_time = [0] * V_sum
    exit_time = [0] * V_sum
    time = 1

    def topologicalSortUtil(v):
        visited[v] = True
        nonlocal time
        entry_time[v] = time
        time += 1
        for i in graph[v]:
            if not visited[i]:
                topologicalSortUtil(i)
        exit_time[v] = time
        time += 1
        stack.insert(0, v)

    for i in range(V_sum):
        if not visited[i]:
            topologicalSortUtil(i)

    return stack


def count_paths(graph, start, end):
    paths = {v: 0 for v in graph}
    paths[start] = 1
    order = topologicalSort(graph)
    for u in order:
        for v in graph[u]:
            paths[v] += paths[u]
    return paths[end]


def is_the_vertex_an_ancestor(graph):
    entry_time = [0] * len(graph)
    exit_time = [0] * len(graph)
    time = 1

    def DFS(vertex, visited=None):
        if visited is None:
            visited = []
        nonlocal time
        entry_time[vertex] = time
        time += 1
        visited.append(vertex)
        for neigh in graph[vertex]:
            if neigh not in visited:
                DFS(neigh, visited)
        exit_time[vertex] = time
        time += 1

    DFS(0)

    q = int(input('Введите количество запросов: '))
    for _ in range(q):
        v, u = map(int, input().split())
        if entry_time[v] < entry_time[u] and exit_time[v] > exit_time[u]:
            print('Да')
        else:
            print('Нет')


def BFS(graph, v):
    queue = [v]
    result = [v]
    d = {v: 0}
    for keys in graph:
        if keys not in d:
            d[keys] = float('inf')

    while queue:
        u = queue.pop(0)
        for neighbour in graph[u]:
            if d[neighbour] == float('inf'):
                d[neighbour] = d[u] + 1
                queue.append(neighbour)
                result.append(neighbour)

    return d, result


graph = read_graph_as_neigh_list()
print(graph[2])
print(graph)
DFS(graph, 0)
print(topologicalSort(graph))
is_the_vertex_an_ancestor(graph)