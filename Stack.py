from typing import Any


class Stack:
    """
    Create a stack data structure. Methods include:

    + `push(item)`: push an item onto the stack.

    + `peek()`: returns the item on top of the stack.

    + `isEmpty()`: returns whether the stack is empty or not.

    + `pop()`: removes the item on top of the stack and returns it.
    """
    __arr: list

    def __init__(self) -> None:
        self.__arr = list()

    def __repr__(self) -> str:
        return str(self.__arr)

    def push(self, item: Any) -> None:
        """
        Push an item onto the stack.

        + `item`: the item to be pushed into the stack.
        """
        self.__arr.append(item)

    def peek(self) -> Any:
        """
        Returns the item on top of the stack.
        """
        if self.isEmpty():
            # If empty stack is peeked, then None type
            # is returned.
            return None
        return self.__arr[-1]

    def isEmpty(self) -> bool:
        """
        Returns whether the stack is empty or not.
        """
        return len(self.__arr) == 0

    def pop(self) -> Any:
        """
        Removes the item on top of the stack and returns it.
        """
        if self.isEmpty():
            raise Exception("Stack is already empty.")
        else:
            end = self.peek()
            self.__arr.pop()
            return end
