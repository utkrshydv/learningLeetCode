# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        rangeSum = 0

        def dfs(root):
            nonlocal rangeSum

            if not root:
                return

            if low <= root.val <= high:
                rangeSum += root.val
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return rangeSum

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

        