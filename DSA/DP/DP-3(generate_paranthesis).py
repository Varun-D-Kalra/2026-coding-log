class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst = []

        def dfs(op, cl, res): # open, close, res is a string
            if op == cl == n:
                lst.append(res)
            
            if op < n:
                dfs(op + 1, cl, res + '(')
            
            if op > cl:
                dfs(op, cl + 1, res + ')')
            

        dfs(0, 0, "")
        return lst

# completed code in 12.40 minutes. Reviewing inefficiencies and learning better approaches.

# REVIEW:EVERY RECURSION CREATES NEW STRING MAKING IT INEFFICIENT, USE A STACK OR A NORMAL LIST TO APPEND PATHS AND AT THE LAST CONVERT TO STRING AND APPEND IN RES.
