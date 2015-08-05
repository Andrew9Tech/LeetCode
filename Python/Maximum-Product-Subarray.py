# Time:  O(n)
# Space: O(1)
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if len(nums) == 0: return 0
        min_temp, max_temp, result = nums[0], nums[0], nums[0]
        for i in xrange(1, len(nums)):
            a, b, c = min_temp*nums[i], max_temp*nums[i], nums[i]
            max_temp = max(max(a, b), c)
            min_temp = min(min(a, b), c)
            if max_temp > result:
                result = max_temp
        return result
        
  if __name__ == "__main__":
    print Solution().maxProduct([2, 3, -2, 4, -1, -6])      
