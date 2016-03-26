class Set:
    def add(self, value):
        pass

    def __iter__(self):
        pass


class SplayTree(Set):
    """
    A SplayTree implementation of Set interface.
    A SplayTree maintains a set of elements drawn from a totally ordered set and allowing membership testing,
    insertions, and deletions (among other operations) at an amortized cost of O(log n) per operation.
    """
    class Node:
        """Node structure."""
        def __init__(self, value, left=None, right=None, parent=None):
            self.value = value
            self.left = left
            if left is not None:
                left.parent = self
            self.right = right
            if right is not None:
                right.parent = self
            self.parent = parent

        def add_left(self, value):
            self.left = SplayTree.Node(value, None, None, self)

        def set_left(self, node):
            self.left = node
            if node is not None:
                node.parent = self

        def add_right(self, value):
            self.right = SplayTree.Node(value, None, None, self)

        def set_right(self, node):
            self.right = node
            if node is not None:
                node.parent = self

    def __init__(self):
        self._root = None

    def _rotate(self, node):
        """Rotate node with respect to its parent"""
        parent = node.parent
        g_parent = parent.parent

        if g_parent is not None:
            if g_parent.left == parent:
                g_parent.set_left(node)
            else:
                g_parent.set_right(node)

        node.parent = g_parent

        if parent.left == node:
            parent.set_left(node.right)
            node.set_right(parent)
        else:
            parent.set_right(node.left)
            node.set_left(parent)

    def _splay(self, node):
        """Reorganize the splay tree so that node is at the root."""
        parent = node.parent

        while parent is not None:
            g_parent = parent.parent
            if g_parent is not None:
                if g_parent.left is parent == parent.left is node:
                    self._rotate(parent)
                else:
                    self._rotate(node)

            self._rotate(node)
            parent = node.parent

        self._root = node
        return node

    def _find(self, value, sub_tree):
        """Find node with the closest value."""
        if sub_tree is None:
            return None
        elif value < sub_tree.value and sub_tree.left is not None:
            return self._find(value, sub_tree.left)
        elif value > sub_tree.value and sub_tree.right is not None:
            return self._find(value, sub_tree.right)
        else:
            return sub_tree

    def find(self, value):
        """Find node by the value and splay tree in it. Return None tree contains no nodes with this value."""
        if self._root is None:
            return None
        else:
            node = self._find(value, self._root)
            if node.value == value:
                self._splay(node)
                return node
            else:
                return None

    def contains(self, value):
        """True if value presented in tree"""
        return self.find(value) is not None

    def split(self, value):
        """Split tree into two subtrees. Elements of left subtree are equal or less than value,
        elements of right one are """
        node = self._find(value, self._root)

        if node is None:
            return None, None

        self._splay(node)

        if node.value <= value:
            right = node.right
            node.right = None
            return node, right
        else:
            left = node.left
            node.left = None
            return left, node

    def merge(self, left, right):
        """Merge two trees into one."""
        if left is None:
            return right

        while left.right is not None:
            left = left.right

        self._splay(left)
        left.set_right(right)

    def add(self, value):
        """Split tree by the value and use it as a root for new tree."""
        left, right = self.split(value)
        self._root = SplayTree.Node(value, left, right)

    def remove(self, value):
        """Remove node from tree."""
        node = self.find(value)

        while node is not None:
            if node.left is not None:
                node.left.parent = None
            if node.right is not None:
                node.right.parent = None
            self.merge(node.left, node.right)
            node = self.find(value)

    def iterate(self, node):
        if node.left is not None:
            yield from self.iterate(node.left)
        yield node.value
        if node.right is not None:
            yield from self.iterate(node.right)

    def __iter__(self):
        self.rec_depth = 0
        if self._root is None:
            return iter([])
        else:
            return self.iterate(self._root)
