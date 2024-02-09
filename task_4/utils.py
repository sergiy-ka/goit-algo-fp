import networkx as nx
import matplotlib.pyplot as plt
import heapq


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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)} 
    plt.figure(figsize=(8, 5))
    plt.title("Binary Tree")
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2000, node_color=colors)
    plt.show()


# Формування бінарної купи з бінарного дерева
def build_heap_from_tree(node):
    heap = []

    def inorder_traversal(node):
        nonlocal heap
        if node:
            inorder_traversal(node.left)
            heap.append((node.val, node.id, node.color))
            inorder_traversal(node.right)
    inorder_traversal(node)
    heapq.heapify(heap)
    return heap


# Побудова вершин та ребер бінарної купи
def add_edges_from_heap(graph, heap, pos, current_index=0, x=0, y=0, layer=1):

    if current_index < len(heap):
        node_value, node_id, node_color = heap[current_index]
        graph.add_node(node_id, color=node_color, label=node_value)

        left_child_index = 2 * current_index + 1
        right_child_index = 2 * current_index + 2

        if left_child_index < len(heap):
            left_child = heap[left_child_index]
            left_child_value, left_child_id, left_child_color = left_child
            graph.add_edge(node_id, left_child_id)
            l = x - 1 / 2 ** layer
            pos[left_child_id] = (l, y - 1)
            add_edges_from_heap(
                graph, heap, pos, left_child_index, x=l, y=y - 1, layer=layer + 1)

        if right_child_index < len(heap):
            right_child = heap[right_child_index]
            right_child_value, right_child_id, right_child_color = right_child
            graph.add_edge(node_id, right_child_id)
            r = x + 1 / 2 ** layer
            pos[right_child_id] = (r, y - 1)
            add_edges_from_heap(
                graph, heap, pos, right_child_index, x=r, y=y - 1, layer=layer + 1)
    return graph


# Візуалізація бінарної купи
def draw_tree_as_heap(tree_root):
    tree = nx.DiGraph()
    heap = build_heap_from_tree(tree_root)
    pos = {heap[0][1]: (0, 0)}
    tree = add_edges_from_heap(tree, heap, pos)

    colors = []
    for i in range(len(heap)):
        colors.append(heap[i][2])
    labels = {}
    for i in range(len(heap)):
        labels[heap[i][1]] = heap[i][0]
    plt.figure(figsize=(8, 5))
    plt.title("Binary tree as Binary Heap")
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2000, node_color=colors)
    plt.show()
