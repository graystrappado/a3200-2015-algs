from sys import stdin, stdout


class Queue:
    def pop(self):
        pass

    def push(self, n):
        pass

    def size(self):
        pass


# implement Queue
class StacksQueue(Queue):
    def __init__(self):
        self._seq = []

    def push(self, a):
        self._seq.append(a)

    def pop(self):
        if self.size() > 0:
            return self._seq.pop()
        else:
            return None

    def size(self):
        return len(self._seq)


class MaxElementQueue(Queue):
    def __init__(self):
        self._maxes = [float("-inf")]
        self._push_max = float("-inf")
        self._pop = StacksQueue()
        self._push = StacksQueue()

    def pop(self):
        if self._pop.size() == 0:
            element = self._push.pop()
            while element is not None:
                self._pop.push(element)
                self._maxes.append(max(element, self._maxes[len(self._maxes) - 1]))
                element = self._push.pop()
            self._push_max = float("-inf")
        value = self._pop.pop()
        if value is not None:
            self._maxes.pop()
            return value
        else:
            return "empty"

    def push(self, n):
        self._push.push(n)
        self._push_max = max(self._push_max, n)

    def size(self):
        return self._push.size() + self._pop.size()

    def max(self):
        value = max(self._push_max, self._maxes[len(self._maxes) - 1])
        if value != float("-inf"):
            return value
        else:
            return "empty"


def parse_line(string, max_element_queue):
    string = string.split("\n")[0]
    if string == "max":
        return str(max_element_queue.max())
    elif string == "pop":
        return str(max_element_queue.pop())
    else:
        command = string.split()
        if len(command) == 2 and command[0] == "push":
            max_element_queue.push(int(command[1]))
            return "ok"
    return "unknown command"

if __name__ == "__main__":
    queue = MaxElementQueue()
    for line in stdin:
        print(parse_line(line, queue))
