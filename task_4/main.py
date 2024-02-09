# Завдання 4. Візуалізація піраміди

from node import Node
from utils import *


if __name__ == "__main__":

    # Створення бінарного дерева
    root = Node(2)
    root.left = Node(7)
    root.left.left = Node(3)
    root.left.right = Node(6)
    root.right = Node(5)
    root.right.left = Node(8)
    root.right.right = Node(1)

    # Відображення бінарного дерева
    draw_tree(root)
    
    # Відображення бінарного дерева як бінарної купи
    draw_tree_as_heap(root)
