# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []

        def dfs(node, number):

            if not node:
                return 
            
            if node.left is None and node.right is None:
                result.append(int(number))
                return 
            if node.left:
                dfs(node.left, number + str(node.left.val))
            if node.right:
                dfs(node.right, number + str(node.right.val))

            number = number[0:len(number) - 1]

        dfs(root, str(root.val))
        return sum(result)

  ## Solved within 16 mins
