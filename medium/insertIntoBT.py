# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        while(1):
            if(val<root.val and root.left == None):
                root.left = TreeNode(val)


tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)


obj = Solution()
root = tree
val = 2
print(obj.searchBST(root,val))
