class Stack:

    def __init__(self, items = [], limit = 100):
        self.items=items
        self.limit=limit

    def isEmpty(self):
        if self.items:
           return False
        else:
            return True
          
    def push(self, item):
        if len(self.items)<100:
            self.items.append(item)
        else:
            print("Error")

    def pop(self):
        pass

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items)== 100:
            return True
        else:
            return False

    def search(self, target):
        if len(self.items)
