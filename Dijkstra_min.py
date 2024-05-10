def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    return graph

#генераторы списков и словаря, множества для обновления уникальных вершин, сортировка
def read_graph_as_neigh_list():
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


def AntiDijkstra(graph, v):
    d = {key: float('-inf') for key in graph}
    w = {key: float('inf') for key in graph}
    visited = []
    end = []
    d[v] = 0
    visited.append((0, v))
    while visited:
        visited.sort()
        c = visited.pop()
        end.append(c[1])
        for neigh, weight in graph[c[1]]:
            if d[c[1]] + weight > d[neigh]:
                d[neigh] = d[c[1]] + weight
                w[neigh] = min(w[c[1]], weight)
                visited.append((d[neigh], neigh))

    return d, w


def AntiDijkstra2(graph, v):
    d = {key: [0] for key in graph}
    visited = []
    end = []
    d[v] = [0]
    visited.append((0, v))
    while visited:
        visited.sort()
        c = visited.pop()
        end.append(c[1])
        for neigh, weight in graph[c[1]]:
            if d[c[1]][-1] + weight > d[neigh][-1]:
                if d[c[1]][0] < weight:
                    d[neigh].append(weight)
                else:
                    d[neigh].append(d[c[1]][-1])
                d[neigh].sort()
                visited.append((d[neigh][-1], neigh))

    res = {key: float('infinity') if len(val) == 1 else val[1] for key, val in d.items()}
    res[v] = 0

    return res


graph = read_graph_as_neigh_list()
d, w = AntiDijkstra(graph, 1)
m = AntiDijkstra2(graph, 1)
print(graph)
print(d)
print(w)
print(m)