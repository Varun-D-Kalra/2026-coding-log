class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(triangle) - 1:
                return triangle[i][j]
            
            if j >= len(triangle[i]):
                return 
            
            memo[(i, j)] = triangle[i][j] +  min(dp(i+1, j), dp(i+1, j+1))

            return memo[(i, j)]
        
        return dp(0, 0)

        # Half an hour. Not optimal, But glad i understood it. Gonna bottom up
