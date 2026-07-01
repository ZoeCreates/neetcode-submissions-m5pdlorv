# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # res 用来存储全局发现的最大直径（边数）
        res = 0 
        
        # 定义一个深度优先搜索（DFS）函数，用于计算每个节点的高度
        def dfs(node):
            # 如果当前节点为空，说明走到了底，高度为 0
            if not node:
                return 0
                
            
            # 使用 nonlocal 关键字，允许我们在内部函数中修改外层定义的 res 变量
            nonlocal res 
            
            # 递归计算左子树的高度（即左子树中最长路径包含的节点数）
            left_height = dfs(node.left)
            # 递归计算右子树的高度
            right_height = dfs(node.right)
            
            # 【核心逻辑】
            # 以当前节点为“拐点”的最长路径，等于“左子树高度 + 右子树高度”
            # 我们将这个值与之前记录的历史最大直径 res 进行对比，把更大的那一个留下来
            res = max(res, left_height+right_height)
            
            # 【返回值】
            # 对上层父节点而言，当前节点只能提供一条路径。
            # 所以返回“自身（算1层）+ 左右子树中较高的一方”，作为当前节点输送给上层的高度
            return 1+max(left_height,right_height)
            
        # 从根节点开始执行 DFS 遍历整棵树
        dfs(root)
       
        
        # 遍历结束后，res 中存的就是整棵树的全局最大直径，直接返回
        return res 
        