class Set:
    def add(self, value):
        pass

    def __iter__(self):
        pass


class UnbalancedBinarySearchTree(Set):

    class Node:
        def __init__(self, value, left=None, right=None, parent=None):
            self.value = value
            self.left = left
            self.right = right
            self.parent = parent

        def set_left(self, value):
            self.left = UnbalancedBinarySearchTree.Node(value, None, None, self)

        def set_right(self, value):
            self.right = UnbalancedBinarySearchTree.Node(value, None, None, self)

    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = UnbalancedBinarySearchTree.Node(value)
        else:
            curr = prev = self.root
            while curr is not None:
                prev = curr
                if value <= curr.value:
                    curr = curr.left
                else:
                    curr = curr.right

            if value <= prev.value:
                prev.set_left(value)
            else:
                prev.set_right(value)

    def contains(self, value):
        curr = self.root

        while curr is not None:
            if value > curr.value:
                curr = curr.right
            elif value < curr.value:
                curr = curr.left
            else:
                return True

        return False

    def iterate(self):
        prev = None
        curr = self.root
        if curr is None:
            yield from ()
            return

        up_from_right = False

        while up_from_right is False:
            while curr.left is not prev and curr.left is not None:
                curr = curr.left

            value = curr.value
            prev = curr

            if curr.right is not None:
                curr = curr.right
            else:
                up_from_right = True
                while up_from_right is True and curr.parent is not None:
                    up_from_right = curr.parent.right is curr
                    prev = curr
                    curr = curr.parent

            yield value

    def __iter__(self):
        # approach with yield, can be inlined into this method too, extracted for example purposes
        return self.iterate()
        # manual approach with next() and StopIteration(). Isn't preferred
        # return TreeGeneratorManual(self)
        # we can also just use the generator from list in this example
        # return self.values.__iter__()
