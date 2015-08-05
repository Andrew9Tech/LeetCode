#
# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
# 
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#

#题意：接上一题，这题要求返回的是所有符合条件的二叉查找树，而上一题要求的是符合条件的二叉查找树的棵数.
#我们上一题提过，求个数一般思路是动态规划，而枚举的话，我们就考虑dfs了。
#  dfs(start, end)函数返回以start，start+1，...，end为根的二叉查找树。

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def dfs(self, start, end):
        if start > end: return [None]
        res = []
        for rootval in range(start, end+1):　　　　　　　　#rootval为根节点的值，从start遍历到end
            LeftTree = self.dfs(start, rootval-1)
            RightTree = self.dfs(rootval+1, end)
            for i in LeftTree:　　　　　　　　　　　　　　　　#i遍历符合条件的左子树
                for j in RightTree:　　　　　　　　　　　　  #j遍历符合条件的右子树
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res
    def generateTrees(self, n):
        return self.dfs(1, n)
        
  if __name__ == "__main__":
    print Solution().generateTrees(3)
