##ocheridi
class Queue():
    def __init__(self):
        self.queue1 = []
    def push(self, item):
        self.queue1.append(item)
    def pop(self):
        if len(self.queue1) == 0:
            return None
        removed = self.queue1.pop(0)
        return removed
 ##stack
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop1(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed
#spiski
class Spiska():
    def __init__(self):
        self.spiska1 = []
    def InsertAtEnd(self, num1):
        self.spiska1.append(num1)
    def InsertAtHead(self, num2):
        self.spiska1.insert(0, num2)
    def Delete(self, num3):
        self.spiska1.remove(num3)
    def DeleteAtHead(self):
        if len(self.spiska1) == 0:
            return None
        removed = self.spiska1.pop(0)
        return removed
    def DeleteAtEnd(self):
        if len(self.spiska1) == 0:
            return None
        removed = self.spiska1.pop()
        return removed
    def SearchIndexElement(self, num4):
        index = self.spiska1.index(num4)
        return index







