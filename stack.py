
class Stack:

    def __init__(self):
        self.data = []

    def isEmpty(self):
        if len(self.data) > 0:
            return False
        else:
            return True

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if not self.isEmpty():
            return self.data[len(self.data) - 1]

    def size(self):
        return len(self.data)
