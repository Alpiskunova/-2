def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    return graph


def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges()
    graph_dict = {}
    vertex_set = set()
    for edge in edge_list:
        vertex_set.update(edge[:2])
    for v in vertex_set:
        graph_dict[v] = set()
    for edge in edge_list:
        graph_dict[edge[0]].add((edge[1], edge[2]))
    return graph_dict


def read_graph_as_neigh_matrix():
    edge_list = read_graph_as_edges()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.update(edge[:2])
    V_num = len(vertex_set)

    res_matrix = [[0 for _ in range(V_num)] for _ in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = edge[1]

    return res_matrix


def Dijkstra(graph, v):
    d = {key: float('inf') for key in graph}
    visited = []
    end = []
    d[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] + neigh[1])
                visited.append(neigh[::-1])

    return d


def Floyd_Warshall(graph):
    v = len(graph)
    d = [[float('inf') for _ in range(v)] for _ in range(v)]
    nxt = [[-1 for _ in range(v)] for _ in range(v)]
    for i in range(v):
        for j in range(v):
            if graph[i][j] != 0:
                d[i][j] = graph[i][j]
                nxt[i][j] = j
    for k in range(1, v):
        for i in range(v):
            for j in range(v):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    nxt[i][j] = nxt[i][k]
    return d, nxt


def pth(i, j, nxt):
    p = [i]
    while nxt[i - 1][j - 1] + 1 != j:
        i = nxt[i - 1][j - 1] + 1
        p.append(i)
    p.append(j)
    return p


graph = read_graph_as_neigh_list_w()
b = Dijkstra(graph, 1)
print(graph)
print(b)