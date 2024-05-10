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


def Dijkstra(graph, v):
    d = {key: float('inf') for key in graph}
    visited = []
    end = []
    d[v] = 1
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[1])
        for neigh, weight in graph[c[1]]:
            if neigh not in end:
                if d[c[1]] * weight < d[neigh]:
                    d[neigh] = d[c[1]] * weight
                visited.append([weight, neigh])

    d[v] = 0
    return d


graph = read_graph_as_neigh_list_w()
b = Dijkstra(graph, 1)
print(graph)
print(b)