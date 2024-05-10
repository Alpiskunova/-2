def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    return graph

#множества, словари, генераторы списков
def read_graph_as_neigh_list_w():
    print("Сначала вводится число (l) - количество ребер. \nЗатем в следующих строках вводится по 1 числу: \nВ 1 строке - вершина, начало ребра \nВо 2 строке - ее цвет \nВ 3 строке- вершина, конец ребра \nВ 4 строке - её цвет \nВ 5 строке - вес ребра")
    print("Введите количество ребер l:")
    edge_list = read_graph_as_edges()
    graph_dict = {}
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[2])
    V_num = len(vertex_set)
    for v in vertex_set:
        graph_dict[v] = set()
    for edge in edge_list:
        graph_dict[edge[0]].add((edge[1], edge[2], edge[3], edge[4]))
    return graph_dict


def Dijkstra(graph, v):
    d = {}
    colors = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = float('inf')
        colors[key] = float('inf')
    d[v] = 0
    colors[v] = 0
    visited.append([0, 0, v])
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[2])
        for neigh in graph[c[2]]:
            if neigh[1] not in end:
                if colors[neigh[1]] == colors[c[2]]:
                    if (d[c[2]] + neigh[3]) < d[neigh[1]]:
                        d[neigh[1]] = (d[c[2]] + neigh[3])
                else:
                    if colors[neigh[1]] == float('inf'):
                        colors[neigh[1]] = colors[c[2]] + 1
                        if (d[c[2]] + neigh[3]) < d[neigh[1]]:
                            d[neigh[1]] = (d[c[2]] + neigh[3])
                    if colors[neigh[1]] <= colors[c[2]]:
                        continue
                    visited.append([colors[neigh[1]], neigh[3], neigh[1]])

    return d, colors


graph = read_graph_as_neigh_list_w()
print(graph)
print(graph[1])
d, c = Dijkstra(graph, 1)
print(d)
print(c)