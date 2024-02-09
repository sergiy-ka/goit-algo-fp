# Завдання 5. Візуалізація обходу бінарного дерева

from node import Node
from utils import *


if __name__ == "__main__":

    node_color = '#ADD8E6'  # Світло-синій

    start_color = '#242D95'  # Темно-синій
    end_color = '#ADD8E6'    # Світло-синій

    # Створення бінарного дерева
    root = Node(2, node_color)
    root.left = Node(7, node_color)
    root.left.left = Node(3, node_color)
    root.left.right = Node(6, node_color)
    root.right = Node(5, node_color)
    root.right.left = Node(8, node_color)
    root.right.right = Node(1, node_color)

    # Відображення початкового стану дерева
    draw_tree(root, "Binary Tree")

    # Відображення дерева після обходу в глибину
    colors = generate_color_gradient(start_color, end_color, count_nodes(root))
    dfs(root, colors)
    draw_tree(root, "Binary Tree (DFS)")

    # Відображення дерева після обходу в ширину
    colors = generate_color_gradient(start_color, end_color, count_nodes(root))
    bfs(root, colors)
    draw_tree(root, "Binary Tree (BFS)")

    # Повертаємо колір вузлів дерева до початкового стану та відображаємо дерево
    change_all_node_color(root, node_color)
    draw_tree(root, "Binary Tree")
