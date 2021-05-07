
def decToHex(d):
    dict = {
    0: '0',1: '1',2: '2',3: '3',4: '4',5: '5',6: '6',7: '7',8: '8',9: '9',10: 'A',
    11:'B',12:'C',13:'D',14:'E',15:'F'
    }
    remainders = []
    while(d>0):
        remainders.append(d%16)
        d =d//16
    hex = ''
    for i in range(len(remainders)-1,-1,-1):
        hex += dict[remainders[i]]
    print(hex)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current


    def insert(self, root,val):
        if(root):
            if(val< root.val):
                root.left = self.insert(root.left,val)
            elif(val > root.val ):
                root.right = self.insert(root.right,val)
        else:
            root = TreeNode(val)
        return root

    def next(self,root):

        if(root):
            if(root.val ==10):
                tmp = root.right
                root = root.left
                root.right = tmp
            self.next(root.left)
            self.next(root.right)

        return root


    def deleteNode(self,root,val):
        if(root):
            # If the val to be deleted is smaller than the root's
            # val then it lies in  left subtree
            if val < root.val:
                root.left = self.deleteNode(root.left, val)

            # If the kye to be delete is greater than the root's val
            # then it lies in right subtree
            elif(val > root.val):
                root.right = self.deleteNode(root.right, val)
            else:
                # delete

                if(root.left is None):
                    temp = root.right
                    root = None
                    return temp

                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp

                temp = minValueNode(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right,temp.val)
        return root



    def traverse(self, root, res):

        if(root):

            res.append(root.val)
            self.traverse(root.left,res)
            self.traverse(root.right,res)
        return res


# [10,5,15,3,7,null,18]
bst = TreeNode(10)
bst.left = TreeNode(5)
bst.right = TreeNode(15)
bst.left.left = TreeNode(3)
bst.left.right =TreeNode(7)
bst.right.right = TreeNode(18)
res = bst.traverse(bst,[])
prev =TreeNode(None)
# c = bst.insert(bst,20)
# print(c.traverse(c,[]))
c = bst.next(bst)
print(c.traverse(c,[]))
# c = bst.insert(bst,1)
# print(c.traverse(c,[]))
