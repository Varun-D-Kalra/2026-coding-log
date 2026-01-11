# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        result, nodes = float('-inf'), []
        
        dummy = head
        while dummy != None:        # used to collect values
            nodes.append(dummy.val)
            dummy = dummy.next
        
        i = -1
        for k in range(0, len(nodes)//2):
            if result < nodes[k] + nodes[i]:
                result = nodes[k] + nodes[i]
            i -= 1
        
        return result


# Solved in 15 minutes from building logic in paper to code 
# got right in 1st submission.

# Solution is O(N) in time and space complexity.

# review : There is room for space optimization
