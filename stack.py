from dataclasses import dataclass, field
from typing import Generic, TypeVar, List, Optional

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
    """A generic Last-In-First-Out (LIFO) stack."""

    _items: List[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> Optional[T]:
        """Remove and return the top item."""
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self) -> Optional[T]:
        """Return the top item without removing it."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check whether the stack is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)