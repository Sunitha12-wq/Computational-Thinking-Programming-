from dataclasses import dataclass, field
from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)

    def push(self, val: T) -> None:
        self.items.append(val)

    def pop(self) -> T:
        return self.items.pop()

    def peek(self) -> T:
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)


@dataclass
class Queue(Generic[T]):
    items: deque[T] = field(default_factory=deque)

    def enqueue(self, val: T) -> None:
        self.items.append(val)

    def dequeue(self) -> T:
        return self.items.popleft()

    def front(self) -> T:
        return self.items[0]

    def size(self) -> int:
        return len(self.items)


# Main
st = Stack[int]()
for num in [5, 10, 15]:
    st.push(num)

print("STACK")
print("Stack:", st.items)
print("Top element:", st.peek())
print("Popped element:", st.pop())
print("Stack after pop:", st.items)
print("Stack size:", st.size())

qu = Queue[str]()
for char in ["X", "Y", "Z"]:
    qu.enqueue(char)

print("\nQUEUE")
print("Queue:", list(qu.items))
print("Front element:", qu.front())
print("Dequeued element:", qu.dequeue())
print("Queue after dequeue:", list(qu.items))
print("Queue size:", qu.size())