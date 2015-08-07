# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
# 解题思路：杨辉三角的求解。
#

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows <= 0:    return []
        if numRows == 1:    return [[1]]
        if numRows == 2:    return [[1], [1, 1]]
        result = [[1], [1, 1]]
        if numRows > 2:
            for i in xrange(2, numRows):
                temp = [1]
                for j in xrange(1, i):
                    temp.append((result[i - 1][j - 1] + result[i - 1][j]))
                temp.append(1)
                #print temp
                result.append(temp)
        return result

if __name__ == "__main__":
    print Solution().generate(5)
