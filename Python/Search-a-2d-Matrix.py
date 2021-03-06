#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,
# 
# Consider the following matrix:
# 
# [
#   [[1,  4,  7, 11, 15],
#   [[2,  5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
#
# Given target = 20, return false.
#

#参见 剑指offer，右上角开始查询

# Time:  O(m + n)
# Space: O(1)
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1

        while i < m and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False

  if __name__ == "__main__":
    matrix = [[1,   4,  7, 11, 15], [2,   5,  8, 12, 19], [3,   6,  9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    print Solution().searchMatrix(matrix, 20)
