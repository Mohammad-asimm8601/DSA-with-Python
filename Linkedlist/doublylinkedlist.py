class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            self.insert_at_head(val)
            return

        current = self.head
        count = 0
        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Positions out of bounds")
            return

        new_node.next = current.next
        new_node.prev = current
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node

    def delete_head(self):
        if self.head is None:
            return
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

    def delete_tail(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.delete_head()
            return
        
        temp = self.head

       
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_at_position(self, pos):
        if self.head is None:
            return "No node is present"

        if pos < 1:
            return "Invalid position"

        if pos == 1:
            self.delete_head()
            return

        temp = self.head
        count = 1

        while temp is not None and count < pos:
            temp = temp.next
            count += 1

        if temp is None:
            return "Position out of range"

        if temp.next is not None:
            temp.next.prev = temp.prev

        temp.prev.next = temp.next
            
        

    def traversal(self):
        if self.head is None:
            return "No node is present"

        temp = self.head
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.insert_at_head(5)
dll.insert_at(15, 2)
dll.delete_head()
dll.delete_tail()
dll.delete_at_position(1)
dll.traversal()
        
        
            
        


