import graphviz
from completbinarytree import MinPriorityQueue
import os
import random
os.environ["PATH"] += os.pathsep + 'D:/learning/Graphviz/bin/'

def visualize_heap(heap):
    """visualize the heap"""
    dot = graphviz.Graph()
    node_list = []

    # convert the number into string
    for i, val in enumerate(heap):
        node_list.append(str(val))

    # Add edges between parent and child nodes
    for i, node in enumerate(node_list):
        parent_index = (i-1) // 2
        if parent_index >= 0:
            dot.edge(node_list[parent_index], node)

    dot.render('tree', view=True)

if __name__=="__main__":
    # Create a MinPriorityQueue and insert some keys
    pq = MinPriorityQueue()
    random_list = [random.randint(0, 100000) for _ in range(7)]
    for j in random_list:
        pq.insert(j)

    # Convert the heap to a list
    cur = pq.tree.root
    heap_list = []
    while cur:
        heap_list.append(cur.key)
        cur = cur.next

    # visualize the tree
    visualize_heap(heap_list)
