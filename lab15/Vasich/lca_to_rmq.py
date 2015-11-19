from math import log2
from sys import stdin


class LCATree:
    def __init__(self, root, vertex_count):
        self._root = root
        self._vert = {root: []}

        segment_tree_size = 2 ** int(log2(2 * vertex_count - 1) + 2) - 1

        self._depths = [(None, float("inf"))] * (2 * vertex_count)
        self._depths_indices = {None: len(self._depths) - 1}

        self._segment_tree = [-1] * segment_tree_size

    def add_vertex(self, v):
        if v not in self._vert:
            self._vert[v] = []

    def add_link(self, v1, v2):
        if v1 not in self._vert:
            self._vert[v1] = []
        if v2 not in self._vert:
            self._vert[v2] = []
        self._vert[v1].append(v2)
        self._vert[v2].append(v1)

    def prepare(self):
        self._dfs(self._root, 0, 0)
        self._construct_segment_tree(0, len(self._depths) - 1, 0)

    def get_mid(self, start, end):
        return (start + end + 1) // 2

    def _dfs(self, v, depth, index):
        self._depths[index] = (v, depth)
        self._depths_indices[v] = index
        index += 1

        for w in self._vert[v]:
            self._vert[w].remove(v)
            depth += 1
            index = self._dfs(w, depth, index)
            depth -= 1
            self._depths[index] = (v, depth)
            index += 1
        return index

    def _construct_segment_tree(self, start, end, index):
        if end - start == 1:
            self._segment_tree[index] = self._depths[start][0]
        else:
            mid = self.get_mid(start, end)
            self._construct_segment_tree(start, mid, 2 * index + 1)
            self._construct_segment_tree(mid, end, 2 * index + 2)

            left_vertex = self._segment_tree[2 * index + 1]
            right_vertex = self._segment_tree[2 * index + 2]

            left_depth = self._depths[self._depths_indices[left_vertex]][1]
            right_depth = self._depths[self._depths_indices[right_vertex]][1]

            if left_depth <= right_depth:
                self._segment_tree[index] = left_vertex
            else:
                self._segment_tree[index] = right_vertex

    def find_lca(self, v1, v2):

        missing_v1 = v1 not in self._depths_indices.keys()
        missing_v2 = v2 not in self._depths_indices.keys()

        msg = "Missing keys:"
        if missing_v1:
            msg += "\tv1 = " + str(v1)
        if missing_v2:
            msg += "\tv2 = " + str(v2)
        if missing_v1 or missing_v2:
            return msg

        start = self._depths_indices[v1]
        end = self._depths_indices[v2]

        if start > end:
            start, end = end, start
        end += 1

        return self._find_lca(start, end, 0, len(self._depths) - 1, 0)

    def _find_lca(self, start, end, seq_start, seq_end, index):
        if start <= seq_start and end >= seq_end:
            return self._segment_tree[index]
        elif start >= seq_end or end <= seq_start:
            return None

        mid = self.get_mid(seq_start, seq_end)
        left_vertex = self._find_lca(start, end, seq_start, mid, 2 * index + 1)
        right_vertex = self._find_lca(start, end, mid, seq_end,  2 * index + 2)

        left_depth = self._depths[self._depths_indices[left_vertex]][1]
        right_depth = self._depths[self._depths_indices[right_vertex]][1]

        if left_depth <= right_depth:
            return left_vertex
        else:
            return right_vertex


if __name__ == "__main__":
    vertices_line = stdin.readline()
    vertices_count = int(vertices_line)
    root_line = stdin.readline().split("\n")[0]

    t = LCATree(root_line, vertices_count)

    i = 0
    while i < vertices_count - 1:
        link_line = stdin.readline().split("\n")[0]
        v1, v2 = link_line.split()
        t.add_link(v1, v2)
        i += 1

    t.prepare()
    print("***")

    for line in stdin:
        link_line = line.split("\n")[0]
        v1, v2 = link_line.split()[:2]
        print(t.find_lca(v1, v2))
