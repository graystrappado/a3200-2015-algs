from lab17.Vasich.dsu import DSUGeneral
import operator


class WeightedGraph:

    def __init__(self):
        self._vert = dict()
        self._edge = dict()
        self._size = 0

    def add_vertex(self, v):
        self._vert.setdefault(v, [])
        return self

    def add_direct_link(self, v1, v2, weight):
        self._edge[tuple(sorted((v1, v2)))] = weight
        self._vert.setdefault(v1, []).append((v2, weight))
        self._vert.setdefault(v2, []).append((v1, weight))
        return self

    def remove_edge(self, v1, v2):
        self._vert[v1] = [v for v in self._vert[v1] if v != v2]
        self._vert[v1] = [v for v in self._vert[v2] if v != v1]
        self._edge.pop(tuple(sorted((v1, v2))))

    def mst(self):
        res = WeightedGraph()
        dsu = DSUGeneral(self._vert)
        edges = sorted(self._edge.items(), key=operator.itemgetter(1))
        for ((v1, v2), weight) in edges:
            if not dsu.same_set(v1, v2):
                dsu.union(v1, v2)
                res.add_direct_link(v1, v2, weight)
        return res

    def weight(self):
        return sum(self._edge.values())

if __name__ == "__main__":
    pass
