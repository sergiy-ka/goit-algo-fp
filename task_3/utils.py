import networkx as nx
import matplotlib.pyplot as plt
import heapq


# Створення зваженого графа
def create_graph(edges):
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    return G


# Візуалізація графа
def draw_graph(G, options, path):
    # Візуалізація графа
    nx.draw(G, **options)
    pos = options['pos']
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Виділити кольором найкоротший шлях
    nx.draw_networkx_nodes(G, pos, nodelist=path,
                           node_color='orange', node_size=1500)
    nx.draw_networkx_edges(G, pos, edgelist=[(
        path[i], path[i+1]) for i in range(len(path)-1)], edge_color='orange', width=1.5)

    # Відображення графа
    plt.show()


# Алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу
def dijkstra(G, start):

    distances = {node: float('infinity') for node in G.nodes}
    distances[start] = 0
    heap = [(0, start)]
    predecessors = {node: None for node in G.nodes}

    while heap:
        current_distance, current_node = heapq.heappop(heap)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in G[current_node].items():
            distance = current_distance + weight['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))
    return distances, predecessors
