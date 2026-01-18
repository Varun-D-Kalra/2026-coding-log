class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:

        if len(lists) == 1:
            k = len(lists[0])
            res = k
            if len(lists[0]) % 2 == 0:
                median = lists[0][(len(lists[0])//2) - 1]
            else:
                median = lists[0][len(lists[0])//2]
            
            return res + median


        def median(a): # pass lists in function
            if len(a) % 2 != 0:
                median_a = a[len(a) // 2]
            else:
                median_a = a[(len(a) // 2) - 1]

            return median_a
        
        def merge(a, b):

            i, j = 0, 0
            res = []

            while i < len(a) and j < len(b):

                if a[i] <= b[j]:
                    res.append(a[i])
                    i += 1
                
                else:
                    res.append(b[j])
                    j += 1
                
            if i < len(a): 
                res.extend(a[i:])
            else:
                res.extend(b[j:])
            
            return res
            


        cost = 0
        while len(lists) > 1:
            m1 = median(lists[0])
            m2 = median(lists[1])
            cost += len(lists[0]) + len(lists[1]) + abs(m1 - m2)
            res = merge(lists[0], lists[1])
            
            lists.pop(0)
            lists.pop(0)

            lists.insert(0, res)
            

        return cost            

# 8 min to understand
# solvedd the whole thing on paper in 22 minus 8 minutes, wrote exact code on paper
# completed coding at 56 minutes. Now debugging
# at 1hr 6 min passed most cases but still failed
# encountered dp issue. fixed all errors but to find the least cost a dp approach is needed, which i dont know at the current date. AHH but its right to calc cost if we were to take 1st 2 lists every time.
