# Time:  O(n)
# Space: O(1)
#
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than [n/2] times.
# 
# You may assume that the array is non-empty and the majority element always exist in the array.
#

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        index, count = 0, 1
        for i in xrange(len(nums)):
            if nums[index] == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    index, count = i, 1
        return nums[index]

if __name__ == "__main__":
    print Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6])
