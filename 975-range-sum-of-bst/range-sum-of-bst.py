# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(root):

            if not root:
                return 0

            rangeSum = 0

            if low <= root.val <= high:
                rangeSum += root.val
            
            rangeSum += dfs(root.left)
            rangeSum += dfs(root.right)

            return rangeSum

        return dfs(root)

        # if root is None:
        #     return 0

        # sum_val = 0

        # if root.val > low:
        #     sum_val += self.rangeSumBST(root.left, low, high)

        # if low <= root.val <= high:
        #     sum_val += root.val

        # if root.val < high:
        #     sum_val += self.rangeSumBST(root.right, low, high)

        # return sum_val

        