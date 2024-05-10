def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    return graph

#Снова пишем через генераторы и словари (там ещё items()), множества
def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges()
    graph_dict = {}
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    for v in vertex_set:
        graph_dict[v] = set()
    for edge in edge_list:
        graph_dict[edge[0]].add((edge[1], edge[2]))
    return graph_dict

def Bellman_Ford(graph, v):
    vertices = len(graph)
    distance = {vertex: float('inf') for vertex in graph}
    distance[v] = 0
    for _ in range(vertices - 1):
        for vertex, neighbors in graph.items():
            for neighbor, weight in neighbors:
                if distance[vertex] != float('inf') and distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            if distance[vertex] != float('inf') and distance[vertex] + weight < distance[neighbor]:
                print("Граф содержит отрицательный цикл")
                return
    return distance

graph = read_graph_as_neigh_list_w()
f = Bellman_Ford(graph, 1)
print(f)