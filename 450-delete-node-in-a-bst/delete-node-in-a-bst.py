# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_succ(self, root):
        root = root.right
        while root!= None and root.left != None:
            root = root.left
        return root

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            else:
                succ = self.get_succ(root)
                root.val = succ.val
                root.right = self.deleteNode(root.right, succ.val)
        return root

        