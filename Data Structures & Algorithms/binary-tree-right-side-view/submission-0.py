# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])
     

        while q:
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                if i == level_size-1:
                    res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res 


            
        # BFS 用的队列，初始放入根节点

        

       
             # 记录当前这一层有多少个节点
            

            
                # 从左到右依次弹出本层节点
                

                # i 是本层最后一个被处理的节点 → 就是这一层最右边的节点
                
                    
                    
                
                # 把下一层的节点按 左→右 顺序加入队列
              
    
  