"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy = {None : None}
    
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy 
            cur = cur.next 
        cur= head
        while cur:
            copy = oldToCopy[cur] # 1. 拿到当前旧节点 cur 对应的新节点 copy
            copy.next = oldToCopy[cur.next] # 2. 将新节点的 next 指向 "旧 next 节点对应的新节点"
            copy.random = oldToCopy[cur.random]  # 3. 将新节点的 random 指向 "旧 random 节点对应的新节点"
            cur = cur.next # 4. 旧链表指针后移
    
        return oldToCopy[head]

    '''
        A deep copy is meant to create completely separate nodes occupying different memory.

        A simple solution:

Pass 1: Create a copy of every node (just values), and store the mapping:
original_node → copied_node
Pass 2: Use this map to connect next and random pointers for each copied node.
    '''
        


    
        