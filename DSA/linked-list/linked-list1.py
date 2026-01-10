# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        lst = []
        dummy = head

        for i in range(0, left-1):
            dummy = dummy.next
        k = dummy

        for i in range(right - left + 1):
            if dummy:
                lst.append(dummy.val)
                dummy = dummy.next
        
        while lst:
            k.val = lst[-1]
            lst.pop()
            k = k.next

        return head
        

## Thought and worked on paper : 20 min 34 sec
## coding time : 20:34 to 29:42

## Solution time complexity: O(n)
## Solution memory complexity: O(n)
