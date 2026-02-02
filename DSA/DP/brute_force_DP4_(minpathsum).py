class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        soln = []

        def dp(a, b, res):
            if a >= len(grid):
                return
            if b >= len(grid[0]):
                return 

            if a == len(grid)-1 and b == len(grid[0]) - 1:
                res += grid[a][b]
                soln.append(res)

            if a <= (len(grid) - 1):
                dp(a + 1, b, res + grid[a][b])
            if b <= (len(grid[0])-1):
                dp(a, b + 1, res + grid[a][b])
            
        dp(0, 0, 0)
        return min(soln)

  # falied due to TLE, learnt memo concept(learned)
