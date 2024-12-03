# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode()
        current = result_head
        ptr_a = list1
        ptr_b = list2
        while ptr_a and ptr_b:
            if ptr_a.val == ptr_b.val:
                current.next = ptr_a
                current = current.next
                current.next = ptr_b
                current = current.next

                ptr_a = ptr_a.next
                ptr_b = ptr_b.next
                current = current.next
            
            elif ptr_a.val < ptr_b.val:
                current.next = ptr_a
                ptr_a = ptr_a.next
                current = current.next
            else:
                current.next = ptr_b
                ptr_b = ptr_b.next
                current = current.next
        
        if ptr_a:
            current.next = ptr_a
        elif ptr_b:
            current.next = ptr_b
        return result_head.next
        


