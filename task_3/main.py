# Завдання 3. Дерева, алгоритм Дейкстри


import networkx as nx
import matplotlib.pyplot as plt
from utils import *


if __name__ == "__main__":

    # Список ребер та їх ваги
    edges = [
        ('Сяйвір', 'Веселун', 40),
        ('Веселун', 'Плутар', 60),
        ('Веселун', 'Фонтаза', 30),
        ('Фонтаза', 'Галактіс', 25),
        ('Фонтаза', 'Плутар', 10),
        ('Плутар', 'Галактіс', 20),
        ('Плутар', 'Сонбрук', 55),
        ('Галактіс', 'Сонбрук', 30),
        ('Сонбрук', 'Мріяр', 20)
    ]

    # Створення зваженого графа
    try:
        G = create_graph(edges)
    except Exception as e:
        print(e)
        exit(1)

    # Назва графа
    plt.title('Графство Зоряних Кришталів')

    # Параметри візуалізації графа
    options = {
        "node_size": 2100,
        "node_color": "skyblue",
        "edgecolors": "black",
        "linewidths": 1,
        "font_size": 8,
        "width": 1,
        "with_labels": True,
        "pos": nx.spring_layout(G, seed=42),
        "font_color": "black",
        "edge_color": "black"
    }

    # Початкова вершина
    start = edges[0][0]

    # Пошук найкоротшого шляху
    try:
        distances, predecessors = dijkstra(G, start)
    except Exception as e:
        print(e)
        exit(1)

    # Вивід результатів
    print(f"\nНайкоротший шлях від {start} до всіх його сусідів:")
    for target, distance in distances.items():
        if target != start:
            print(f"{target}: {distance} одиниць")
    print(
        f"\nВибір найкоротшого шляху від {start} до {edges[-1][1]}:")
    for target, distance in distances.items():
        path = [target]
        while predecessors[target] is not None:
            target = predecessors[target]
            path.insert(0, target)
        print(f"Від {start} до {path[-1]}: {distance} одиниць, Шлях: {path}")

    # Візуалізація графа
    try:
        draw_graph(G, options, path)
    except Exception as e:
        print(e)
        exit(1)
