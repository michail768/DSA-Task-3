class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def enqueue(self, item):
        # Check for overflow
        if (self.rear + 1) % self.capacity == self.front:
            print("Queue Overflow")
            return
        elif self.front == -1:  # First element
            self.front = self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item

    def dequeue(self):
        # Check for underflow
        if self.front == -1:
            print("Queue Underflow")
            return None
        temp = self.queue[self.front]
        if self.front == self.rear:  # Queue has only one element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return temp