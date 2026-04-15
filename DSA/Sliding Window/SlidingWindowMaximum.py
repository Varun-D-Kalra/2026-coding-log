from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):

            # This is an indicator of old elements. Remove it.
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove smaller ele from end to append a big val
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # after deletion now its the right spot to add the ele
            dq.append(i)

            # Now update result if window is valid.
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
