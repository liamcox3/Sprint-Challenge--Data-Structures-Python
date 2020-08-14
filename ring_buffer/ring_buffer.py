class RingBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity

    # class __Full(RingBuffer):
    #     def append(self, x):
    #         self.cur = (self.cur + 1) % self.capacity
    #         self.buffer[self.cur] = x

    #     def get(self):
    #         return self.buffer[self.cur:] + self.buffer[:self.cur]

    def append(self, item):
        self.buffer.append(item)
        if len(self.buffer) == self.capacity:
            self.cur = 0

    def get(self):
        return self.buffer
