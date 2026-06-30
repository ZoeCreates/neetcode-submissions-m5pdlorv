# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0  # <--- 这是外层函数的变量
        
        def dfs(node):
            nonlocal res  # <--- 声明这里的 res 指向的是外层的那个 res
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # 如果不用 nonlocal，Python 会把下面这行赋值语句当成：
            # 在 dfs 函数内部创建了一个新的、只在 dfs 内部有效的局部变量 res
            res = max(res, left_height + right_height) 
            
            return 1 + max(left_height, right_height)
            
        dfs(root)
        return res