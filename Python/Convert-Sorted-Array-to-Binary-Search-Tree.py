# Time:  O(n)
# Space: O(logn)
#
# Given an array where elements are sorted in ascending order, 
# convert it to a height balanced BST.
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        length = len(nums)
        if length == 0: return None
        root = TreeNode(nums[length/2])
        root.left = self.sortedArrayToBST(nums[0:length/2])
        root.right = self.sortedArrayToBST(nums[length/2 + 1:])
        return root
    
if __name__ == "__main__":
    num = [1, 2, 3]
    result = Solution().sortedArrayToBST(num)
    print result.val
    print result.left.val
    print result.right.val
