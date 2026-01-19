# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        dum = head
        while dum:
            arr.append(dum)
            dum = dum.next

        if k > len(arr):
            return
        
        arr[k-1].val, arr[-k].val = arr[-k].val, arr[k-1].val
        return head


# review : NGL it took me way lot of time, even if the solution was super simple
# O(n), O(n)
# memory can be O(1)

# Time taken is like 30 + minutes to think a solution, once it clicked 3 mins to code
