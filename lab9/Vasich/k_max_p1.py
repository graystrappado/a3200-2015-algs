class Queue:
    def pop(self):
        pass

    def push(self, n):
        pass

    def size(self):
        pass


class MinHeap(Queue):
    def __init__(self, k):
        self._size = 0
        self._k = k
        self._seq = []

    def pop(self):
        if self._size > 0:
            self._seq[0], self._seq[self._size - 1] = self._seq[self._size - 1], self._seq[0]
            value = self._seq.pop()
            self._size -= 1

            i = 0
            while i < self._size:
                left = float("inf")
                right = float("inf")

                if 2 * i + 1 < self._size:
                    left = self._seq[2 * i + 1]
                if 2 * i + 2 < self._size:
                    right = self._seq[2 * i + 2]

                if left < right:
                    m = left
                    i_m = 2 * i + 1
                else:
                    m = right
                    i_m = 2 * i + 2

                if self._seq[i] > m:
                    self._seq[i], self._seq[i_m] = self._seq[i_m], self._seq[i]
                    i = i_m
                else:
                    break

            return value

        else:
            return "empty"

    def push(self, n):
        self._seq.append(n)
        self._size += 1

        i = self._size - 1
        while i > 0:
            if self._seq[(i - 1) // 2] > self._seq[i]:
                self._seq[(i - 1) // 2], self._seq[i] = self._seq[i], self._seq[(i - 1) // 2]
                i = (i - 1) // 2
            else:
                break

        if self._size > self._k:
            self.pop()

    def size(self):
        return self._size

    def max_list(self):
        return self._seq
