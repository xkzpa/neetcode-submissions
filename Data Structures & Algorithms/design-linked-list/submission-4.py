class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0
        
    def get(self, index: int) -> int:          
        if index < self.size:
            tmp = self.head
            if tmp:
                inx = 0
                while inx != index:
                    tmp = tmp.next
                    inx += 1
                return tmp.val
        return -1
        
    def addAtHead(self, val: int) -> None:
        if self.head:
            tmp = self.head
            self.head = ListNode(val)
            self.head.next = tmp
            tmp.prev = self.head
            if not tmp.next:
                self.tail = tmp
        else:
            self.head = ListNode(val)
            self.tail = self.head
        self.size += 1


    def addAtTail(self, val: int) -> None:
        tmp = self.tail
        if tmp:            
            self.tail = ListNode(val)
            self.tail.prev = tmp
            tmp.next = self.tail
            
        else:
            # no items in the list at all
            self.tail = ListNode(val)
            self.head = self.tail
        self.size += 1
        
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < self.size:
            tmp = self._getListNodeAtIndex(index)
            
            n = ListNode(val)
            n.prev = tmp.prev
            n.next = tmp            

            rp = tmp.prev
            if rp:
                rp.next = n
            
            tmp.prev = n
            if index == 0:
                self.head = n
            # if index == self.size - 1:
            #     self.tail = n
            
            self.size += 1
        elif index == self.size:
            self.addAtTail(val)
            
    def _getListNodeAtIndex(self, index):
        tmp = self.head
        if tmp:
            inx = 0
            while inx < index:
                tmp = tmp.next
                inx += 1
        return tmp
    
    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            tmp = self._getListNodeAtIndex(index)
            p = tmp.prev
            n = tmp.next
            if p:
                p.next = n
            else:
                self.head = n
            if n:
                n.prev = p
            else:
                self.tail = p
            self.size -= 1
                