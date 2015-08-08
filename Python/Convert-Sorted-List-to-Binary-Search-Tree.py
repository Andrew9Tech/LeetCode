# Time:  O(n)
# Space: O(logn)
#
# Given a singly linked list where elements are sorted in ascending order, 
# convert it to a height balanced BST.
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        Array, p = [], head
        while p:
            Array.append(p.val)
            p = p.next
        return self.sortedArrayToBST(Array)
    
    def sortedArrayToBST(self, Array):
        length = len(Array)
        if length == 0: return None
        root = TreeNode(Array[length/2])
        root.left = self.sortedArrayToBST(Array[0:length/2])
        root.right = self.sortedArrayToBST(Array[length/2 + 1:])
        return root

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    result = Solution().sortedListToBST(head)
    print result.val
    print result.left.val
    print result.right.val
