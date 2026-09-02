from data_structures import Stack, Queue


# Stack
stack: Stack[int] = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack top:", stack.peek())
print("Stack pop:", stack.pop())
print("Stack size:", stack.size())


# Queue
queue: Queue[str] = Queue()

queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Charlie")

print("Queue front:", queue.front())
print("Queue dequeue:", queue.dequeue())
print("Queue size:", queue.size())