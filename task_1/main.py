# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

from node import *
from linked_list import *


if __name__ == "__main__":

    # Створення зв'язного списку №1
    llist_1 = LinkedList()

    llist_1.insert_at_beginning(5)
    llist_1.insert_at_beginning(10)
    llist_1.insert_at_beginning(15)
    llist_1.insert_at_end(20)
    llist_1.insert_at_end(25)

    # Друк зв'язного списку №1
    print("\nЗв'язний список №1:")
    llist_1.print_list()

    # Реверсування зв'язного списку №1
    llist_1.reverse_list()
    print("\nЗв'язний список №1 після реверсування:")
    llist_1.print_list()

    # Сортування зв'язного списку №1
    llist_1.insertion_sort()
    print("\nЗв'язний список №1 після сортування:")
    llist_1.print_list()

    # Створення зв'язного списку №2
    llist_2 = LinkedList()

    llist_2.insert_at_end(102)
    llist_2.insert_at_end(33)
    llist_2.insert_at_end(18)
    llist_2.insert_at_end(23)

    # Друк зв'язного списку №2
    print("\nЗв'язний список №2:")
    llist_2.print_list()

    # Сортування зв'язного списку №2
    llist_2.insertion_sort()
    print("\nЗв'язний список №2 після сортування:")
    llist_2.print_list()

    # Об'єднання двох відсортованих списків
    llist_merged = LinkedList.merge_sorted_lists(llist_1, llist_2)
    print("\nОб'єднаний відсортований зв'язний список:")
    llist_merged.print_list()
