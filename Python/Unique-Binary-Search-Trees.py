#
# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
# 
# For example,
# Given n = 3, there are a total of 5 unique BST's.
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#

###############           
# Time:  O(2^n)
# Space: O(1)
#TimeOut
class Solution1:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        if n == 0 or n == 1:    return 1
        elif n == 2: return 2
        else:
            result = 0
            for i in range(n):
                result += self.numTrees(i) * self.numTrees(n - i - 1)
            return result

###############           
# Time:  O(n^2)
# Space: O(n)
class Solution2:
    # @return an integer
    def numTrees(self, n):
        counts = [1, 1]
        for i in xrange(2, n + 1):
            count = 0
            for j in xrange(i):
                count += counts[j] * counts[i - j - 1]
            counts.append(count)
        return counts[-1]
    
if __name__ == "__main__":
    print Solution2().numTrees(19)
