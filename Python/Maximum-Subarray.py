# Time:  O(n)
# Space: O(1)
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# 
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
# 
# click to show more practice.
# 
# More practice:
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#

#最大子序列和问题,剑指offer


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        ThisSum = 0
        MaxSum = -10000
        for i in range( 0, len(A) ):
            if ThisSum < 0:
                ThisSum = 0
            ThisSum = ThisSum + A[ i ]
            MaxSum = max( ThisSum, MaxSum )
        return MaxSum
        
  if __name__ == "__main__":
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4      
        
