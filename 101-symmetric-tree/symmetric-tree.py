# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        q = deque([(root.left, root.right)])

        while q:

            left, right = q.popleft()

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False

            q.append((left.right, right.left))
            q.append((left.left, right.right))

        return True
        # def dfs(left, right):
        #     if not left and not right:
        #         return True
        #     if not left or not right:
        #         return False

        #     return (left.val == right.val and
        #             dfs(left.left, right.right) and
        #             dfs(left.right, right.left))

        # return dfs(root.left, root.right)
