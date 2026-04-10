# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 想到用两个pointer历遍两个list，每一轮都进行比较
        # 哪个node大就插到哪个后面


        # wrtie a dummy node sp that you have a fixed starting point 
        #that is guaranteed to exist.
        dummy = cur =  ListNode(0)
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2= list2.next
            cur = cur.next 
        
        cur.next= list1 or list2 

        
        return dummy.next

            
            
   

    





        