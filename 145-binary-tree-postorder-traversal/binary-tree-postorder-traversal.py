# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        myList = []
        if root is not None:
            myList.extend(self.postorderTraversal(root.left))
            myList.extend(self.postorderTraversal(root.right))
            myList.append(root.val)
        return myList