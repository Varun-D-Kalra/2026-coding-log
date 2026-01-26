class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return res
        
        else:
            for i in range(3, numRows+1, 1):
                new_arr = [1] * i
                for j in range(1, len(new_arr) - 1):
                    new_arr[j] = res[-1][j - 1] + res[-1][j]
                res.append(new_arr)
            return res


    # solved in 18 mins. O(n) O(n**2)
