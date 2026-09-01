class ListNode:
    def __init__(self, val: int):
        self.next = None
        self.val = val
        

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get(self, index: int) -> int:
        n = self._getNodeAtIndex(index)
        if n:
            return n.val
        return -1

    def addAtHead(self, val: int) -> None:
        nn = ListNode(val)
        if self.head:
            tmp = self.head
            nn.next = tmp
        else:
            self.tail = nn
        self.head = nn
        self.size += 1
                        
    def addAtTail(self, val: int) -> None:
        nn = ListNode(val)
        if self.tail:
            tmp = self.tail
            tmp.next = nn
        self.tail = nn
        self.size += 1
        
    def _getNodeAtIndex(self, index: int) -> ListNode:
        if index < self.size:
            inx = 0
            tmp = self.head
            while tmp.next and index > inx:
                tmp = tmp.next
                inx += 1
            return tmp
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size and index >= 0:
            if index == 0:
                self.addAtHead(val)
            elif index == self.size:
                self.addAtTail(val)
            else:
                n = self._getNodeAtIndex(index-1)
                nx = n.next
        
                nn = ListNode(val)
                n.next = nn
                nn.next = nx
                self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            node = self._getNodeAtIndex(index-1 if index > 0 else 0)
            if index == 0:
                self.head = node.next
                node.next = None
            elif index == self.size - 1:                
                self.tail = node
                node.next = None
            else:
                node.next = node.next.next
                    
            self.size -= 1
        