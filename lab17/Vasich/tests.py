import unittest
from random import sample, choice, randrange, shuffle, getrandbits
from lab17.Vasich.kruskal import WeightedGraph
from lab17.Vasich.dsu import DSUGeneral


class TestKruskal(unittest.TestCase):

    def check_dsu(self, dsu, sets, number_of_test):
        for _ in range(number_of_test):
            s = choice(sets)
            item1, item2 = choice(s), choice(s)
            self.assertTrue(dsu.same_set(item1, item2))             # true for items from the same category

        for _ in range(number_of_test):
            s1, s2 = sample(sets, 2)
            item1, item2 = choice(s1), choice(s2)
            self.assertFalse(dsu.same_set(item1, item2))            # false for items from different categories

    def test_dsu(self):

        number_of_categories = 100                                  # initial number_of_categories
        new_number_of_categories = 10                               # will be merged into new_number_of_categories later
        number_of_items = number_of_categories + 10 ** 5
        max_item = number_of_items + 10 ** 8
        number_of_test = 10 ** 3

        items = sample(range(max_item), number_of_items)
        sets = [[item] for item in items[:number_of_categories]]    # make each category non-empty
        for item in items[number_of_categories:]:                   # then populate
            choice(sets).append(item)

        dsu = DSUGeneral(items)

        for (leader, s) in ((choice(s), s) for s in sets):          # for each category pick leader
            for item in s:                                          # and merge all items in category
                dsu.union(item, leader)

        self.check_dsu(dsu, sets, number_of_test)

        shuffle(sets)
        sets, tail = sets[:new_number_of_categories], sets[new_number_of_categories:]
        for (s, t) in ((choice(sets), t) for t in tail):
            dsu.union(choice(s), choice(t))
            s.extend(t)

        self.check_dsu(dsu, sets, number_of_test)

    def check_spanning(self, tree, graph):
        dsu = DSUGeneral(tree._vert)
        for v in tree._vert:
            for u, _ in tree._vert[v]:
                dsu.union(u, v)
        self.assertTrue(dsu.single_set())
        self.assertEqual(len(tree._edge), len(graph._vert) - 1)

    def test_mst_manually(self):

        graph = WeightedGraph()
        graph. \
            add_direct_link(1, 2, 1).add_direct_link(1, 3, 1).add_direct_link(1, 4, 1). \
            add_direct_link(2, 3, 1).add_direct_link(2, 4, 1).add_direct_link(3, 4, 1)
        mst = graph.mst()
        self.check_spanning(mst, graph)
        self.assertEqual(mst.weight(), 3)

        graph = WeightedGraph()
        graph. \
            add_direct_link(2, 3, 1).add_direct_link(2, 4, 2).add_direct_link(3, 4, 3). \
            add_direct_link(1, 2, 3).add_direct_link(1, 3, 2).add_direct_link(1, 4, 1)
        mst = graph.mst()                               # 1-4, 2-3, 2-4 or 1-3, 1-4, 2-3
        self.check_spanning(mst, graph)
        self.assertEqual(mst.weight(), 4)
        s = {(1, 4), (2, 3), (2, 4)}.symmetric_difference(set(mst._edge))
        self.assertTrue(s == {} or s == {(1, 3), (2, 4)})

    def test_mst_random(self):

        graph = WeightedGraph()
        number_of_vertices = 10 ** 3
        max_value = number_of_vertices + 10 ** 2
        number_of_chords = number_of_vertices // 2
        branching_factor = 4
        delta_weight = 30

        vs = sample(range(max_value), number_of_vertices)
        trees = [[v] for v in vs]
        guaranteed = set()
        possible = set()
        min_weight, max_weight = 0, 0
        while len(trees) > 1:                                                   # spanning tree of the graph
            min_weight, max_weight = max_weight, max_weight + delta_weight      # in each iteration weight is increased
            nodes_on_level = max(len(trees) // branching_factor, 1)
            trees, tail = trees[:nodes_on_level], trees[nodes_on_level:]
            for (tree, t) in ((choice(trees), t) for t in tail):                # Cut property:
                [u], [v] = sample(tree, 1), sample(t, 1)                        # Let S be any subset of vertices,
                w = randrange(min_weight, max_weight)                           # and let e be the min cost edge
                graph.add_direct_link(u, v, w)                                  # with exactly one endpoint in S.
                tree.extend(t)                                                  # Then the MST contains e.
                e = tuple(sorted((u, v)))
                if nodes_on_level > 1:                      # So the lightest edges must be present in the graph's MST
                    guaranteed.add(e)
                else:                                       # There will be more edges within the last range
                    possible.add(e)
        i = 0
        extralarge_weight = max_weight + delta_weight
        while i < number_of_chords:
            (u, v) = sorted(sample(vs, 2))
            if (u, v) not in graph._edge:
                if getrandbits(1):                          # Here they are
                    graph.add_direct_link(u, v, randrange(min_weight, max_weight))          # Cycle property:
                    possible.add((u, v))                                                    # Let C be any cycle in G,
                else:                                                                       # and let f be the max cost
                    graph.add_direct_link(u, v, randrange(max_weight, extralarge_weight))   # edge belonging to C.
                i += 1                                                                      # Then the MST
        mst = graph.mst()                                                                   # does not contain f.
        result = set(mst._edge)
        self.check_spanning(mst, graph)
        self.assertTrue(guaranteed <= result)               # Cut property: contains all min edges of spanning forest
        self.assertTrue(result - guaranteed <= possible)    # Cycle property: contains no heavy chords
