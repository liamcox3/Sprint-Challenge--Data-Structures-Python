class RingBuffer:
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.cur = 0

    # class __Full(RingBuffer):
    #     def append(self, x):
    #         self.cur = (self.cur + 1) % self.capacity
    #         self.buffer[self.cur] = x

    #     def get(self):
    #         return self.buffer[self.cur:] + self.buffer[:self.cur]

    def append(self, item):
        self.buffer[self.cur] = item
        self.cur = self.cur + 1
        if self.cur == self.capacity:
            self.cur = 0

    def get(self):
        return [item for item in self.buffer if item is not None]
