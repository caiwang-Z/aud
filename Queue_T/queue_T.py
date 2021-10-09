class Queues_T:
    def __init__(self, size=10):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0
        self.front = 0

    def push(self, element):
        if self.is_filled():
            raise IndexError('Queue_T is full')
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element

    def pop(self):
        if self.is_empty():
            raise IndexError('Queue_T is empty')
        else:
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]

    def is_empty(self):
        return self.front == self.rear

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front

if __name__ == '__main__':

    q = Queues_T(5)
    print(q.is_empty())
