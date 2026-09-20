# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        myList = []
        if root is not None:
            myList.append(root.val)
            myList.extend(self.preorderTraversal(root.left))
            myList.extend(self.preorderTraversal(root.right))

        return myList
      
        