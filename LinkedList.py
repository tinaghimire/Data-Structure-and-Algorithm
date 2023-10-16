#Node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node
    
    #Insert at beginning
    def remove_at_beginning(self, data):
        self.head = self.head.next

    #Inser at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            
    #Search
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False
    
name = LinkedList()
name.insert_at_beginning("Kristina")
name.insert_at_beginning("Kristina")
name.insert_at_beginning("Kristina")
print(name)


            
        