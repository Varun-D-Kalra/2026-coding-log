class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        dummy = self.head
        count = 0
        while dummy:
            if count == index:
                return dummy.val
            dummy = dummy.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)              
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        dum = self.head
        while dum.next:
            dum = dum.next
        dum.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        dum = self.head
        i = 0
        while dum and i < index - 1:
            dum = dum.next
            i += 1
        if not dum:
            return
        node = Node(val)
        node.next = dum.next
        dum.next = node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        dum = self.head
        i = 0
        while dum and i < index - 1:
            dum = dum.next
            i += 1
        if dum and dum.next:
            dum.next = dum.next.next


    # Review : I missed building node class, so i had to fix at places where i wrote Mylinked list to build a new node. 

    # Forgot to record the time, but im sure it took like 40 mins
  # truth : I was lazy debugging, copilot fixed the changes i knew i had to do lol.
    
