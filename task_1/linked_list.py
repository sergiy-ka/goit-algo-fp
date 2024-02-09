from node import *


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Функція, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами
    def reverse_list(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    # Алгоритм сортування вставками (Insertion sort) для однозв'язного списку
    def insertion_sort(self):
        if self.head is None:
            return
        sorted_head = None
        cur = self.head
        while cur:
            next_node = cur.next
            sorted_head = self.insert_in_sorted_order(sorted_head, cur)
            cur = next_node
        self.head = sorted_head

    def insert_in_sorted_order(self, sorted_head, new_node):
        if sorted_head is None or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node
        cur = sorted_head
        while cur.next and cur.next.data < new_node.data:
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node
        return sorted_head

    # Функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список
    def merge_sorted_lists(llist1, llist2):
        merged_list = LinkedList()
        current1 = llist1.head
        current2 = llist2.head
        while current1 is not None and current2 is not None:
            if current1.data <= current2.data:
                merged_list.insert_at_end(current1.data)
                current1 = current1.next
            else:
                merged_list.insert_at_end(current2.data)
                current2 = current2.next
        while current1 is not None:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next
        while current2 is not None:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next
        return merged_list
