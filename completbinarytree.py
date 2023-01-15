class Node:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

class CompleteBinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def get_parent_index(self, index):
        """Return the index of the parent of the node at the given index,
           or -1 if the node is the root."""
        if index == 0 or self.size < index:
            return -1
        parent_index = (index+1) // 2 - 1
        return parent_index

    def get_left_child_index(self, index):
        """Return the index of the left child of the node at the given index,
           or -1 if the node has no left child or the index larger than the tree size."""
        left_child_index = 2 * (index+1) - 1
        if left_child_index > self.size:
            return -1
        return left_child_index


    def get_right_child_index(self, index):
        """Return the index of the right child of the node at the given index,
           or -1 if the node has no right child or the index larger than the tree size.."""
        right_child_index = 2 * (index+1)
        if right_child_index > self.size:
            return -1
        return right_child_index

    def get_by_index(self, index):
        """return the node at the given index and return its key,
           or None if the index is invalid."""
        current = self.root
        current_index = 0
        while current is not None:
            if index == current_index:
                return current.key
            current = current.next
            current_index += 1
        return None

    def get_parent(self, index):
        """return the parent of the node at the given index and return its key,
           or None if the index is invalid."""
        index_p = self.get_parent_index(index)

        if index_p == -1:
            return None

        return self.get_by_index(index_p)

    def get_left_child(self, index):
        """return the left child of the node at the given index and return its key,
           or None if the index is invalid."""
        index_l = self.get_left_child_index(index)

        if index_l == -1:
            return None

        return self.get_by_index(index_l)

    def get_right_child(self, index):
        """return the right child of the node at the given index and return its key,
           or None if the index is invalid."""
        index_r = self.get_right_child_index(index)

        if index_r == -1:
            return None

        return self.get_by_index(index_r)

class MinPriorityQueue:
    def __init__(self):
        self.tree = CompleteBinaryTree()
        self.size = 0

    def insert(self, key):
        """insert a new key to the priority queue"""
        self.tree.size += 1
        self.size += 1
        new_node = Node(key)
        if self.tree.root is None:
            self.tree.root = new_node
            return
        curr_node = self.tree.root
        while True:
            if key > curr_node.key:
                if curr_node.next is None:
                    curr_node.next = new_node
                    return
                curr_node = curr_node.next
            else:
                key, curr_node.key = curr_node.key, key
                if curr_node.next is None:
                    curr_node.next = Node(key)
                    return
                curr_node = curr_node.next

    def delMin(self):
        """removes and returns the minimum key from the priority queue"""
        if self.tree.root is None:
            return None
        min_key = self.tree.root.key
        self.tree.root = self.tree.root.next
        self.tree.size -= 1
        self.size -= 1
        return min_key






