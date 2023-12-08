import time
import random
import matplotlib.pyplot as plt
from problem_1 import SinglyLinkedList
from BST import BST
from AVL import AVL

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def build_time_experiment(data_structure_class, data_subset):
    start_time = time.time()
    data_structure = data_structure_class()
    for item in data_subset:
        data_structure.insert(item)
    end_time = time.time()
    return end_time - start_time

def search_time_experiment(data_structure, search_items):
    start_time = time.time()
    for item in search_items:
        try:
            if isinstance(data_structure, SinglyLinkedList):
                data_structure.iterative_find(item)
            else:
                data_structure.find(item)
        except ValueError:
            pass
    end_time = time.time()
    return end_time - start_time




if __name__ == "__main__":
    file_path = 'file.txt'
    # n_values = list(range(12, 500))
    n_values = [2**i for i in range(3, 12)]

    lines = read_file(file_path)

    build_times_sll = []
    build_times_bst = []
    build_times_avl = []
    search_times_sll = []
    search_times_bst = []
    search_times_avl = []

    for n in n_values:
        if n <= len(lines):
            subset = random.sample(lines, n)
            search_items = random.sample(subset, 5)

            # SinglyLinkedList build time
            sll_time = build_time_experiment(SinglyLinkedList, subset)
            build_times_sll.append(sll_time)

            # BST build time
            bst_time = build_time_experiment(BST, subset)
            build_times_bst.append(bst_time)

            # AVL build time
            avl_time = build_time_experiment(AVL, subset)
            build_times_avl.append(avl_time)

            # SinglyLinkedList search time
            sll_search_time = search_time_experiment(SinglyLinkedList(), search_items)
            search_times_sll.append(sll_search_time)

            # BST search time
            bst_search_time = search_time_experiment(BST(), search_items)
            search_times_bst.append(bst_search_time)

            # AVL search time
            avl_search_time = search_time_experiment(AVL(), search_items)
            search_times_avl.append(avl_search_time)

    # Plotting the results
    plt.figure(figsize=(10, 6))

    # Build times subplot
    plt.subplot(2, 1, 1)
    plt.plot(n_values, build_times_sll, label='SinglyLinkedList')
    plt.plot(n_values, build_times_bst, label='BST')
    plt.plot(n_values, build_times_avl, label='AVL')
    plt.yscale('log')
    plt.title('Build Times')
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()

    # Search times subplot
    plt.subplot(2, 1, 2)
    plt.plot(n_values, search_times_sll, label='SinglyLinkedList')
    plt.plot(n_values, search_times_bst, label='BST')
    plt.plot(n_values, search_times_avl, label='AVL')
    plt.yscale('log')
    plt.title('Search Times (5 items)')
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()

    plt.tight_layout()
    plt.show()
