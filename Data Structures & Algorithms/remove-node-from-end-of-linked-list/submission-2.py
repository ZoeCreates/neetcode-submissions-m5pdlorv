# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #1. Create a dummy node pointing to the head (helps handle deletion of the first node).
        dummy = ListNode(0, head)
        #Set two pointers:left at dummy,right at head
        #helps handle deletion of the first node 
        left = dummy 
        right = head 

        #3. Move right forward n steps.
        while n >0:
            right = right.next 
            n-=1
        
        #4.Move both pointers until right reaches the end.
        while right:
            left=left.next
            right = right.next 

        
        #5. Now left.next is the node to delete → skip it by doing      left.next = left.next.next.
        left.next = left.next.next

        return dummy.next 


'''
如果没有 dummy，当你要删除第一个节点（head）时，它前面是没有节点的，你必须写专门的 if 逻辑来处理。

加上 dummy 后，head 也有了前驱节点（就是 dummy）！这样无论删第 1 个节点还是第 N 个节点，操作完全一致。

(在链表结构里，head 变量保存的就是链表第 1 个节点的引用（指针）)

'''










        