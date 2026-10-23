class Node:
    def __init__(self, val):
        self.val  = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def traversal(self):
        if not self.head:
            print("SLL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next

    def insert(self, pos, val):
        new_node = Node(val)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            count = 0
            while curr is not None and count < pos-1:
                curr = curr.next
                count += 1
            new_node.next = curr.next
            curr.next = new_node
    
    def delete(self, val):
        temp = self.head
        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return
            else:
                found = False
                prev = None
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    prev = temp
                    temp = temp.next
                if found:
                    prev.next = temp.next
                    return
                else:
                    print("Node not found")

sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.append(47)
sll.insert(0, 5)
sll.insert(2, 25)
sll.insert(7, 55)
sll.delete(5)
sll.delete(40)
sll.traversal()