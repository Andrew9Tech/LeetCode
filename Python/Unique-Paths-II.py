# Time:  O(m * n)
# Space: O(m * n)
#
# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
# 
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
# 
# Note: m and n will be at most 100.
#
class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, grid):
        rows = len(grid)
        cols = len(grid[0])
         
        # base case
        dp = [[0 for j in xrange(cols)] for i in xrange(rows)]
        for i in xrange(cols):
            if grid[0][i] == 0: dp[0][i] = 1
            else: break
        for i in xrange(rows):
            if grid[i][0] == 0: dp[i][0] = 1
            else: break
         
        # dynamic programming
        for i in xrange(1, rows):
            for j in xrange(1, cols):
                dp[i][j] = 0 if grid[i][j] == 1 else dp[i - 1][j] + dp[i][j - 1]
        return dp[rows - 1][cols - 1]
