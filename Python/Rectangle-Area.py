
# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
# Rectangle Area
# Assume that the total area is never beyond the maximum possible value of int.
#
# Credits:
# Special thanks to @mithmatt for adding this problem, creating the above image and all test cases.

# 参考此链接 http://bookshadow.com/weblog/2015/06/08/leetcode-rectangle-area/

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        SUM = (C - A)*(D - B) + (G - E)*(H - F)
        COM = (max(min(G, C) - max(E, A), 0))*(max(min(D, H) - max(B, F), 0))
        return SUM - COM
