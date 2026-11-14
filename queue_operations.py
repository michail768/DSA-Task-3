class Queue:

  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.append(item)
    print(f"Enqueued: {item}")

  def dequeue(self):
    if not self.is_empty():
      item = self.items.pop(0)
      print(f"Dequeued: {item}")
      return item
    print("Queue Underflow")
    return None

  def is_empty(self):
    return len(self.items) == 0