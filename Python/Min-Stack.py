#
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# 题目大意：
# 设计一个栈，支持在常数时间内push，pop，top，和取最小值。
#
# push(x) -- 元素x压入栈
# pop() -- 弹出栈顶元素
# top() -- 获取栈顶元素
# getMin() -- 获取栈中的最小值
#
#
# 解题思路来源：http://bookshadow.com/weblog/2014/11/10/leetcode-min-stack/
# 解题思路：
# “双栈法”，栈stack存储当前的所有元素，minStack存储栈中的最小元素。
#
# 在操作元素栈stack的同时，维护最小值栈minStack。
#
# 对于push（x）操作：
#
# stack.push( x )
# minStack.push( min( minStack.top(), x ) )
#
#
# 注意事项（Tricks）：
# leetcode OJ对于该题目的内存限制比较严苛，直接使用双栈法容易出现Memory Limit Exceeded（MLE）
# 
# 可以使用下面的优化解决此问题，minStack存储元组（minVal, count），分别记录当前的最小值和出现次数。
# 
# 如果新增元素x与最小值栈顶的minVal相同，则只更新count。


class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        #最小值栈 （最小值，出现次数）
        self.minStack = []

    def push(self, x):
        self.stack.append(x)
        #如果 新增值x == 最小值栈顶的值
        if len(self.minStack) and x == self.minStack[-1][0]:
            #最小值栈顶元素次数+1
            self.minStack[-1] = (x, self.minStack[-1][1] + 1)
        #如果 最小值栈为空，或者新增值 < 最小值栈顶的值
        elif len(self.minStack) == 0 or x < self.minStack[-1][0]:
            #x入最小值栈
            self.minStack.append((x, 1))

    def pop(self):
        #如果 栈顶值 == 最小值栈顶值
        if self.top() == self.getMin():
            #如果 最小值栈顶元素次数 > 1
            if self.minStack[-1][1] > 1:
                #最小值栈顶元素次数 - 1
                self.minStack[-1] = (self.minStack[-1][0], self.minStack[-1][1] - 1)
            else:
                #最小值栈顶元素弹出
                self.minStack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1][0]
        
