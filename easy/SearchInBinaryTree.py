# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        if(val == root.val):
            return root
        search = []
        while(root is not None):
            if(root):
                if(root.val == val):
                    return root
            if(root.right!=None):
                search.append(root.right)
            if(root.left ==None and len(search)>0):
                root = search.pop()
            else:
                root = root.left
        return None


tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)


obj = Solution()
root = tree
val = 2
print(obj.searchBST(root,val))
