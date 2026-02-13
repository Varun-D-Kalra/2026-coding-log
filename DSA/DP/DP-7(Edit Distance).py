class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m, n = len(word1), len(word2)

        cache =  [ [float('inf')] * n for _ in range(m) ]

        def dp(i, j):

            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i
            
            if cache[i][j] != float('inf'):
                return cache[i][j]
            
            if word1[i] == word2[j]:
                cache[i][j] = dp(i + 1, j + 1)
            
            else:
                ins = dp(i, j + 1)
                delete = dp(i + 1, j)
                replace = dp(i + 1, j + 1)

                cache[i][j] =  1 + min(ins, delete, replace)

            return cache[i][j]
            
        return dp(0, 0)

## I saw the solution and then coded it from memory. I now feel this is easy and can be done again.
