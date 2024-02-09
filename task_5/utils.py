import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.colors import LinearSegmentedColormap


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, tree_name="Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(tree_name)
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2000, node_color=colors)
    plt.show()

# Обхід в глибину та зміна кольору вузлів
def dfs(node, colors):
    if node is not None:
        current_color = colors.pop(0)
        change_node_color(node, current_color)
        dfs(node.left, colors)
        dfs(node.right, colors)

# Обхід в ширину та зміна кольору вузлів
def bfs(node, colors):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        change_node_color(node, colors.pop(0))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Зміна кольору вузла
def change_node_color(node, color):
    if node is not None:
        node.color = color

# Зміна кольору всіх вузлів
def change_all_node_color(node, color):
    if node is not None:
        node.color = color
        change_all_node_color(node.left, color)
        change_all_node_color(node.right, color)

# Генерація градієнту кольорів
def generate_color_gradient(start_color='#242D95', end_color='#ADD8E6', num_steps=1):
    cmap = LinearSegmentedColormap.from_list(
        'custom_gradient', [start_color, end_color], N=num_steps)
    colors = [cmap(i) for i in range(num_steps)]
    colors = [
        f'#{int(r*255):02X}{int(g*255):02X}{int(b*255):02X}' for r, g, b, _ in colors]
    return colors

# Підрахунок кількості вузлів у дереві
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
