# Завдання 6: Жадібні алгоритми та динамічне програмування

from copy import deepcopy


def greedy_algorithm(budget, products):
    result = {}
    items = deepcopy(products)
    # співвідношення калорій до вартості
    for item in items:
        items[item]["calories_per_cost"] = items[item]["calories"] / \
            items[item]["cost"]
    # сортуємо за співвідношенням калорій до вартості
    items = sorted(
        items.items(), key=lambda x: x[1]["calories_per_cost"], reverse=True)
    # вибираємо страви, поки не перевищимо бюджет
    for item, item_value in items:
        count = budget // item_value["cost"]
        if count > 0:
            result[item] = {}
            result[item]["quantity"] = count
            result[item]["total_cost"] = count * item_value["cost"]
            result[item]["total_calories"] = count * item_value["calories"]
            budget = budget % item_value["cost"]
    return result


def dynamic_programming(budget, products):
    items = deepcopy(products)
    product_names = list(items.keys())
    val = [items[food]["calories"] for food in product_names]
    wt = [items[food]["cost"] for food in product_names]
    n = len(val)

    K = [[0 for x in range(budget + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    result = {}
    i = n
    j = budget
    while i > 0 and j > 0:
        if K[i][j] != K[i-1][j]:
            product_name = product_names[i-1]
            if product_name not in result:
                result[product_name] = {
                    'quantity': 0,
                    'total_cost': 0,
                    'total_calories': 0
                }
            result[product_name]['quantity'] += 1
            result[product_name]['total_cost'] += wt[i-1]
            result[product_name]['total_calories'] += val[i-1]
            j -= wt[i-1]
        else:
            i -= 1
    return result


if __name__ == "__main__":
    budget = 310
    products = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    greedy_algorithm_result = greedy_algorithm(budget, products)
    dynamic_programming_result = dynamic_programming(budget, products)

    print(f"Budget: {budget}")
    print(
        f"Greedy algorithm (Total calories = {sum([v['total_calories'] for v in greedy_algorithm_result.values()])}): {greedy_algorithm_result}")
    print(
        f"Dynamic programming (Total calories = {sum([v['total_calories'] for v in dynamic_programming_result.values()])}): {dynamic_programming_result}")
