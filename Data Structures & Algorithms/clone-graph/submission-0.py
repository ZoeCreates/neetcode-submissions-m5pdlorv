"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


'''
浅拷贝（Wrong）：如果你直接 return node，或者只是新建了一个节点却依然指向旧节点的邻居（neighbors），这相当于只是复用了同一块内存地址。修改新图会影响旧图。

深拷贝（Right）：你需要全新创建图里的每一个 Node 对象（val 值和原来一样），并且让新节点之间的邻居关系（neighbors 数组）也完全对应旧节点之间的连接关系。旧图和新图在内存里必须是完全独立的两套对象。

图是有环/双向连接的：节点 1 的邻居有 2，节点 2 的邻居也有 1。如果你盲目递归克隆邻居，代码就会进入无限循环（死循环）。

2. 节点会被多次访问：节点 3 可能既是 1 的邻居，也是 2 的邻居。你需要保证节点 3 只被克隆一次，第二次遇到它时，直接使用之前已经创建好的新节点，而不是重复创建。

为了解决上面的问题，我们需要一个 哈希表（Map/HashMap）：

Key：原图节点 old_node

Value：对应的克隆节点 new_node
'''

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #如果输入的节点为空，直接返回 None
        if not node:
            return None
        
        old_to_new = {}

        def dfs(curr_node):
            #检查当前节点是否已经在哈希表中：如果在：说明这个节点之前已经被克隆过了，直接返回哈希表里的 new_node（防止死循环和重复创建）。
            if curr_node in old_to_new:
                return old_to_new[curr_node]
            
            #如果不在：
            #新建一个克隆节点
            copy = Node(curr_node.val)
            #把映射关系记入哈希表
            old_to_new[curr_node] = copy

            #遍历原节点的每一个邻居 neighbor，递归调用克隆函数，把克隆出来的邻居节点加入到copy.neighbors 列表里
            for neightbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neightbor))
            return copy
        
        return dfs(node)
        

            



        