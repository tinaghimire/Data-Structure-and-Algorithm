#Node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top == None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        
    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
        


        

        