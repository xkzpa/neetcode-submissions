# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if not head:
            return None
        if head.next != None:
            res = []            
            while head.next:
                res.append(head)
                head = head.next

            res[-1].next = None
            head.next = res[-1]
            for i in range(len(res)-1, 0, -1):
                res[i-1].next = None
                res[i].next = res[i-1]

        return head