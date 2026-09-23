# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False

        req_sum = targetSum - root.val

        # checking at leaf node
        if root.left is None and root.right is None:
            return req_sum == 0

        left = self.hasPathSum(root.left, req_sum)
        right = self.hasPathSum(root.right, req_sum)

        return left or right

      
        return left or right
        