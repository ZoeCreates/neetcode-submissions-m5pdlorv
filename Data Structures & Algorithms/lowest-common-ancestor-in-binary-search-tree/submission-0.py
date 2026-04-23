# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        情况 A：$p$ 和 $q$ 都比当前节点小说明它们全都在左边。既然都在左边，当前的 root 肯定不是“最近”的祖先（左儿子比它更近），所以你要往左跳。
        情况 B：$p$ 和 $q$ 都比当前节点大说明它们全都在右边。同理，你要往右跳。
        情况 C：一小一大（分叉了）这就是你高亮后面提到的 "split occurs"。如果一个在左，一个在右，或者当前节点正好等于其中一个，那么当前的 root 就是你要找的 LCA。
        """

        if not root or not p or not q:
            return None 
        if(max(p.val, q.val)<root.val):
            return self.lowestCommonAncestor(root.left,p,q)
        elif(min(p.val,q.val)> root.val):
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root 
        
        




        