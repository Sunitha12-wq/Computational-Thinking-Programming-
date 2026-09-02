from dataclasses import dataclass, field
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")


@dataclass
class Queue(Generic[T]):
    """A generic First-In-First-Out (FIFO) queue."""

    _items: List[T] = field(default_factory=list)

    def enqueue(self, item: T) -> None:
        """Add an item to the rear of the queue."""
        self._items.append(item)

    def dequeue(self) -> Optional[T]:
        """Remove and return the front item."""
        if self.is_empty():
            return None
        return self._items.pop(0)

    def front(self) -> Optional[T]:
        """Return the front item without removing it."""
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        """Check whether the queue is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self._items)