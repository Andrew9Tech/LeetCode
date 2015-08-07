# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?


class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        row = [1]
        for i in range(1, rowIndex+1):
            row = list(map(lambda x,y: x+y, [0]+row, row + [0]))
        return row
