# Завдання 7: Використання методу Монте-Карло


import random
import matplotlib.pyplot as plt
from collections import defaultdict

# Аналітичні розрахунки
analytical_probabilities = {2: 0.0278, 3: 0.0556, 4: 0.0833, 5: 0.1111,
                            6: 0.1389, 7: 0.1667, 8: 0.1389, 9: 0.1111, 10: 0.0833, 11: 0.0556, 12: 0.0278}

if __name__ == "__main__":
    # Кількість кидків кубиків
    n = 1_000_000

    # Створення словника для зберігання кількості кидків для кожної суми
    sums = defaultdict(int)

    # Кидки кубиків
    for i in range(n):
        # Визначення суми чисел, які випали на кубиках
        sum_ = random.randint(1, 6) + random.randint(1, 6)
        sums[sum_] += 1

    # Визначення ймовірностей кожної суми
    probabilities = {k: v / n for k, v in sums.items()}

    # Сортування за ключем
    probabilities = dict(sorted(probabilities.items()))

    # Порівняння результатів з аналітичними розрахунками
    print("\nПорівняння результатів обчислення імовірності за методом Монте-Карло з аналітичними розрахунками:")
    print(f"| {'-'*10:^10} | {'-'*30:^30} | {'-'*30:^30} |")
    print(
        f"| {'Сума':^10} | {'Імовірність (Монте-Карло), %':^30} | {'Імовірність (аналіт.), %':^30} |")
    print(f"| {'-'*10:^10} | {'-'*30:^30} | {'-'*30:^30} |")
    for k, v in probabilities.items():
        print(
            f"| {k:^10} | {round(v*100,2):^30} | {round(analytical_probabilities[k]*100,2):^30} |")
    print(f"| {'-'*10:^10} | {'-'*30:^30} | {'-'*30:^30} |")

    # Побудова графіка з результатами методу Монте-Карло
    plt.bar(probabilities.keys(), probabilities.values())
    plt.xlabel('Сума')
    plt.ylabel('Імовірність')
    plt.title('Імовірність суми при киданні двох кубиків (Монте-Карло)')
    plt.show()
