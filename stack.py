class Stack:
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == [] 

    def pop(self):
        return self._items.pop()

    def push(self , item):
        return self._items.append(item)

    def peek(self):
        n = len(self._items)
        return self._items[ n - 1]     

    def size(self):
        return len(self._items)            
        