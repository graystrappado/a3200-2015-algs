class DSUIndexed:
    def __init__(self, size):
        self._parent = list(range(size))
        self._rank = [0] * size

    def find(self, x):
        if self._parent[x] != x:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return

        if self._rank[x_root] < self._rank[y_root]:
            self._parent[x_root] = y_root
        else:
            self._parent[y_root] = x_root
            if self._rank[x_root] == self._rank[y_root]:
                self._rank[x_root] += 1
        return self

    def same_set(self, x, y):
        return self.find(x) == self.find(y)

    def single_set(self):
        return all(DSUIndexed.same_set(self, x, y) for (x, y) in zip(self._parent[1:], self._parent[:-1]))

    def reset(self):
        self._parent = [i for i, v in enumerate(self._parent)]
        self._rank = [0] * len(self._rank)


class DSUGeneral(DSUIndexed):
    def __init__(self, collection):
        self._id = dict()
        for item in collection:
            self._id.setdefault(item, len(self._id))
        super().__init__(len(self._id))

    def add(self, item):
        if item not in self._id:
            i = self._id.setdefault(item, len(self._id))
            super()._parent.append(i)
            super()._rank.append(i)
        return self

    def union(self, x, y):
        return super().union(self._id[x], self._id[y])

    def same_set(self, x, y):
        return super().same_set(self._id[x], self._id[y])
