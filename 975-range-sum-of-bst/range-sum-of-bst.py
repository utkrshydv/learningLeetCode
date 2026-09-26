# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        

        def dfs(root):
            if root is None:
                return 0
            total = 0
            if low <= root.val <= high:
                total += root.val
            
            total += dfs(root.left)
            total += dfs(root.right)

            return total


        return dfs(root)
        