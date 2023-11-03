"""
"""


class Stack:
    def __init__(self):
      self.items = []
      
    def is_empty(self):
        return not self.items
      
    def push(self, item):
      self.items.append(item)
      
    def pop(self):
      return self.items.pop()
      
    def peek(self):
      return self.items[-1]
      
    def __str__(self):
        return f'{self.items}, len({len(self.items)})'

    def __repr__(self):
        return f'{self.items}, len({len(self.items)})'
        
        
if __name__ == "__main__":
    s = Stack()
    print(f"{s}")
    print(f'is_empty: {s.is_empty()}')
    s.push(3)
    s.push(7)
    print(f"{s}")
    print(f'is_empty: {s.is_empty()}')
    s.push(5)
    print(f"{s}")
    print(f'peek: {s.peek()}')
    print(f"{s}")
    print(f'pop: {s.pop()}')
    print(f"{s}")
    