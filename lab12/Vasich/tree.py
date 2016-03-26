
class Set:
    def add(self, value):
        pass

    def __iter__(self):
        pass


class UnbalancedBinarySearchTree(Set):

    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def add(self, value):
        if self.parent is None:
            self.parent = self
            self.value = value
            return self

        curr = self
        while True:
            if value <= curr.value:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = UnbalancedBinarySearchTree(value, curr)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = UnbalancedBinarySearchTree(value, curr)
                    break
        return self

    def contains(self, value):
        curr = self
        while curr:
            if value == curr.value:
                return True
            curr = curr.left if value <= curr.value else curr.right
        return False

    def iterate(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

    def __iter__(self):
        if self.parent is None:
            return iter([])
        return self.iterate()


if __name__ == "__main__":
    pass
