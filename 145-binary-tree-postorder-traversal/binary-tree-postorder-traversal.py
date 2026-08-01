# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        mylist=[]
        if root != None:
            mylist.extend(self.postorderTraversal(root.left))
            mylist.extend(self.postorderTraversal(root.right))
            mylist.append(root.val)
        return mylist
        