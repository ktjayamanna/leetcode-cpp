# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        """
        Reverses a linked list.

        This function takes the head of a singly linked list as an argument
        and returns the head of the reversed linked list.

        :param head: The head of the singly linked list.
        :type head: ListNode
        :return: The head of the reversed linked list.
        :rtype: ListNode
        """
        ptr_left = None
        ptr_right = head
        while ptr_right:
            tmp = ptr_right.next
            ptr_right.next = ptr_left
            ptr_left = ptr_right
            ptr_right = tmp
        return ptr_left



        
        


