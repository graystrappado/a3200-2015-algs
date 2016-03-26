from lab14.Vasich.topological_sorting import Graph
import unittest
import random


def _has_cycle(graph):
    flag = {v: "to_traverse" for v in graph._vert}

    def dfs(v):
        if flag[v] != "to_traverse":
            return flag[v] != "traversed"
        flag[v] = "traversing"
        if any(dfs(w) for w in graph._vert[v]):
            return True
        flag[v] = "traversed"
        return False

    return any(dfs(v) for v in graph._vert)


class TestTopologicalSorting(unittest.TestCase):

    def _check(self, graph):
        result = graph.topological_sort()
        if result:
            self.assertEqual(len(result), len(graph._vert))
            self.assertFalse(any(v in graph._vert[g]
                             for i, v in enumerate(result) for g in result[i:]))
        else:
            self.assertTrue(_has_cycle(graph))

    def test_manual(self):
        g = Graph()
        g.\
            add_directed_link(1, 2).add_directed_link(1, 3).\
            add_directed_link(3, 5).add_directed_link(3, 0).\
            add_directed_link(101, 0).add_directed_link(4, 10).\
            add_directed_link(3, 101)
        self._check(g)      # without cycles

        g.add_directed_link(1, 4).add_directed_link(10, 1)
        self._check(g)      # with cycle

    def test_random(self):
        for i in range(100):
            graph = Graph()
            for (v1, v2) in ((random.randint(0, 20), random.randint(0, 20)) for _ in range(15)):
                graph.add_directed_link(v1, v2)
            self._check(graph)
