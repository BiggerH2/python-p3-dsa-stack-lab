class Stack:
    def __init__(self, iterable=None, limit=None):
        self.stack = list(iterable) if iterable else []
        self.limit = limit

    def push(self, value):
        if self.limit is None or len(self.stack) < self.limit:
            self.stack.append(value)
        else:
            raise StackFullException("Stack Overflow - Stack is full")

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def empty(self):
        return len(self.stack) == 0

    def full(self):
        if self.limit is not None:
            return len(self.stack) == self.limit
        else:
            return False

    def search(self, value):
        try:
            index = self.stack.index(value)
            return len(self.stack) - index - 1
        except ValueError:
            return -1

class StackFullException(Exception):
    pass
