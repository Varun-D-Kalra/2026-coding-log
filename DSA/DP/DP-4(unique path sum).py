class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        if obstacleGrid[0][0] == 0 and obstacleGrid == [[0]]:
            return 1

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        res = [[-1 for _ in range(n)] for _ in range(m)]

        def dp(a, b):
            if a >= m or b >= n:
                return 0
            if obstacleGrid[a][b] == 1:
                return 0
            if a == m - 1 and b == n - 1:
                return 1

            if res[a][b] != -1:
                return res[a][b]
                
            res[a][b] = dp(a + 1, b) + dp(a, b + 1)
            return res[a][b]

        dp(0, 0)
        return res[0][0]
