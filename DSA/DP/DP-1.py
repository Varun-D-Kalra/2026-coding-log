class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def recurssion(k, memo):
            if k == 1:
                return 1
            if k == 2:
                return 2
            if k in memo.keys():
                return memo[k]
            else:
                memo[k] = recurssion(k-1,memo) + recurssion(k-2, memo)

            return memo[k]
        
        res = recurssion(n, memo)
        return res
    # solved in 12 minutes
    # speed : O(n)
    # space : O(n)
    # used recurrsive - memoization method
    
