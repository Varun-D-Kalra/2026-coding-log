from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]

            if i == n:  # reached the top
                return 0

            cost = float('inf')

            # Jump to i+1
            if (i + 1) <= n:
                cost = min(cost, costs[i] + (1**2) + dp(i + 1))

            # Jump to i+2
            if (i + 2) <= n:
                cost = min(cost, costs[i+1] + (2**2) + dp(i + 2))

            # Jump to i+3
            if (i + 3) <= n:
                cost = min(cost, costs[i+2] + (3**2) + dp(i + 3))

            memo[i] = cost
            return memo[i]

        return dp(0)
