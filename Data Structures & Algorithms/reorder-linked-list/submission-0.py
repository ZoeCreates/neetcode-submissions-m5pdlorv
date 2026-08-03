# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        '''
        Find the middle:

        Use slow and fast pointers.
        When fast reaches the end, slow will be at 
        the  midpoint.

        '''
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        '''
        Reverse the second half:

        Start from slow.next.
        Reverse it using the standard linked-list      reversal approach with prev and tmp variables.



        '''
        
        second = slow.next
        prev = slow.next = None
        while second: 
            tmp = second.next
            second.next = prev
            prev= second 
            second = tmp 
        

        '''
        Merge the two lists:

Take a node from first half.
Take a node from the reversed second half.
Continue until second is exhausted.

        '''

        first, second = head, prev 
        while second:
            tmp1,tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1 
            first, second = tmp1,tmp2

        