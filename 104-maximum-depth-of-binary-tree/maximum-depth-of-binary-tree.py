# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if node is None:
                return 0

            l_hght = solve(node.left)
            r_hght = solve(node.right)

            return 1 + max(l_hght, r_hght)

        return solve(root)
        # if not root:
        #     return 0
        
        # level = 0
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level

        

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        