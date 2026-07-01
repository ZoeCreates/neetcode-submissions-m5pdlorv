# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            # 空节点高度为 0，且它是平衡的
            if not node:
                return 0
            
            # 1. 计算左子树高度
            left_height = dfs(node.left)
            if left_height == -1: 
                return -1  # 左子树已经不平衡了，直接提前退出
            
            # 2. 计算右子树高度
            right_height = dfs(node.right)
            if right_height == -1: 
                return -1  # 右子树已经不平衡了，直接提前退出
            
            # 3. 检查当前节点是否平衡
            # 如果左右子树高度差大于 1，说明当前节点不平衡，返回 -1
            if abs(left_height - right_height) > 1:
                return -1
            
            # 4. 如果平衡，返回当前节点的高度
            return max(left_height, right_height) + 1

        # 如果最终结果不是 -1，说明整棵树都是平衡的
        return dfs(root) != -1