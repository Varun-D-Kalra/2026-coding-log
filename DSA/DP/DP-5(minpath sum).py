class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}

        m, n = len(grid), len(grid[0]) 

        if m == n == 1:
            return grid[m-1][n-1]

        def dp(a, b):
            if a >= m or b >= n: # out of bounds
                return float('inf')

            if a == m-1 and b == n-1: # Base case to return value
                return grid[a][b]

            if (a, b) in memo:  # sends values from memo
                return memo[(a, b)]

            memo[(a, b)] = grid[a][b] + min(dp(a+1, b), dp(a, b+1))
            return memo[(a, b)]

        dp(0, 0)
        return memo[(0, 0)]

        # Top - Down DP 
        # time = O(m * n)
        # space = O(m* n)
