


# 题目大意：
# 给定一棵二叉搜索树（BST），寻找BST中两个给定节点的最近公共祖先（LCA）。
#
# 根据维基百科对LCA的定义：“节点v与w的最近公共祖先是树T上同时拥有v与w作为后继的最低节点（我们允许将一个节点当做其本身的后继）”
#
# 例如，题目描述的样例中，节点2和8的最近公共祖先（LCA）是6。另一个例子，节点2和4的LCA是2，因为根据LCA的定义，一个节点可以是其本身的后继。
#
# 解题思路：
# 根据BST的性质，左子树节点的值＜根节点的值，右子树节点的值＞根节点的值
# 记当前节点为node，从根节点root出发
#
# 若p与q分别位于node的两侧，或其中之一的值与node相同，则node为LCA
#
# 否则，若p的值＜node的值，则LCA位于node的左子树
#
# 否则，LCA位于node的右子树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  迭代版本
class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        while (p.val - root.val) * (q.val - root.val) > 0:
            root = [root.left, root.right][p.val > root.val]
        return root
        
  # 递归版本      
  class Solution2:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if (p.val - root.val) * (q.val - root.val) <= 0:
            return root
        elif p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
