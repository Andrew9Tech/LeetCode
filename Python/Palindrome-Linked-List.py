
# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if (head == None):
            return True
        fast = slow = head;
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        p, last = slow.next, None
        while p:
            temp =  p.next
            p.next = last
            p, last = temp, p
        
        p1, p2 =last, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
        
        return p1 is None
