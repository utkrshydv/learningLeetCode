# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        mylist=[]
        if root!=None:
            mylist.extend(self.inorderTraversal(root.left))
            mylist.append(root.val)
            mylist.extend(self.inorderTraversal(root.right))
        return mylist

        myList = []
        if root is not None:
            myList.extend(self.inorderTraversal(root.left))
            myList.append(root.val)
            myList.extend(self.inorderTraversal(root.right))
        return myList