



# 题目大意：
# 翻转一棵二叉树。
#
# 测试样例见题目描述。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is None:
            return None
        root.right, root.left = root.left, root.right
        if root.right:
            self.invertTree(root.right)
        if root.left:
            self.invertTree(root.left)
        return root
