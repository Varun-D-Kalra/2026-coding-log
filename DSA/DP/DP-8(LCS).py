class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        cache = [[float('-inf')] * n for _ in range(m)]

        def dp(i, j):
            if i == m or j == n:
                return 0
            
            if cache[i][j] != float('-inf'):
                return cache[i][j]
            
            
            if text1[i] == text2[j]:
                cache[i][j] = 1 + dp(i + 1, j + 1)
            
            else:
                cache[i][j] = max(dp(i, j+1), dp(i + 1, j))
            
            return cache[i][j]

            
        return dp(0,0)
      # it was fun solving this, it felt easy for me. Im sure i was done in 30 minutes
