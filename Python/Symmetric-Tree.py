# Time:  O(n)
# Space: O(h), h is height of binary tree
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
# 
# For example, this binary tree is symmetric:
# 
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#

# 解题思路来源：http://www.cnblogs.com/zuoyuan/p/3747174.html
# 解题思路：(递归)
# 需要用一个help函数，当然也是递归的。
# 当存在左右子树时，判断左右子树的根节点值是否相等，如果相等继续递归判断左子树根的右子树根节点和右子树根的左子树根节点
# 以及左子树根的左子树根节点和右子树根的右子树根节点的值是否相等。然后一直递归判断下去就可以了。

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Iterative solution
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        
        while stack:
            p, q = stack.pop(), stack.pop()
            
            if p is None and q is None:
                continue
            
            if p is None or q is None or p.val != q.val:
                return False
            
            stack.append(p.left)
            stack.append(q.right)
            
            stack.append(p.right)
            stack.append(q.left)
            
        return True
        
# Recursive solution
class Solution2:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricRecu(root.left, root.right)
    
    def isSymmetricRecu(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(2)
    root.left.left, root.right.right = TreeNode(3), TreeNode(3)
    root.left.right, root.right.left = TreeNode(4), TreeNode(4)
    print Solution0().isSymmetric(root)
