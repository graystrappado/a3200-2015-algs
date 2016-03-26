from math import inf
import heapq


class WeightedGraph:
    def __init__(self):
        self._vert = {}
        self._prev = {}
        self._dist = {}

    def add_vertex(self, v):
        self._vert.setdefault(v, [])

    def add_direct_link(self, v1, v2, weight):
        self._vert.setdefault(v1, []).append((v2, weight))
        self._vert.setdefault(v2, [])

    def paths(self, w):
        self._dijkstra(w)
        res = {v: [] for v in self._vert}
        for (v, path) in res.items():
            if self._dist[v] == inf:
                continue
            while v is not None:
                path.append(v)
                v = self._prev[v]
            path.reverse()
        return res

    def _dijkstra(self, w):
        for v in self._vert:
            self._prev[v] = None
            self._dist[v] = inf
        self._dist[w] = 0
        q = [(self._dist[v], v) for v in self._vert]
        heapq.heapify(q)

        while q:
            _, u = heapq.heappop(q)
            for (v, weight) in self._vert[u]:
                if self._dist[v] > self._dist[u] + weight:
                    q.remove((self._dist[v], v))
                    heapq.heapify(q)
                    self._dist[v] = self._dist[u] + weight
                    self._prev[v] = u
                    heapq.heappush(q, (self._dist[v], v))


if __name__ == "__main__":
    pass