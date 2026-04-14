# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #用dfs，recursive base case
        #root指向linked list的head，用的是pointer存每个node的refernece
        if root == None:
            return 
        
        #交换
        temp = root.left 
        root.left = root.right
        root.right = temp 


        #dfs
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root




        
        
        

        