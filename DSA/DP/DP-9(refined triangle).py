class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        n = len(triangle)

        for j in range(len(triangle[n-1])):
            memo[(n-1, j)] = triangle[n-1][j]
        
        for i in range(n - 2, -1, -1):
            for j in range(0, len(triangle[i])):
                memo[(i, j)] = triangle[i][j] + min(memo[(i+1, j)], memo[i+1, j+1])
        
        return memo[(0, 0)]

        # optimised but still not best, im glad hahaa. Gpt showed me the actual one and damn the answer is in front of me but i did not see. Cool code...
