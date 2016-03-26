from collections import defaultdict

class Graph:
    def __init__(self):
        self._vert = {}

    def add_vertex(self, v):
        self._vert.setdefault(v, [])
        return self

    def add_directed_link(self, v1, v2):
        self._vert.setdefault(v1, []).append(v2)
        self._vert.setdefault(v2, [])
        return self

    def topological_sort(self):
        flag = {v: "white" for v in self._vert}
        result = []

        def dfs(v):
            if flag[v] != "white":
                return flag[v] == "black"
            flag[v] = "gray"
            if not all(dfs(w) for w in self._vert[v]):
                return False
            flag[v] = "black"
            result.append(v)
            return True

        return result[::-1] if all(dfs(v) for v in self._vert) else None


