

# 参考：http://bookshadow.com/weblog/2015/04/29/leetcode-isomorphic-strings/
# 题目大意：
# 给定两个字符串s和t，判断它们是否是同构的。
#
# 如果字符串s可以通过字符替换的方式得到字符串t，则称s和t是同构的。
#
# 字符的每一次出现都必须被其对应字符所替换，同时还需要保证原始顺序不发生改变。两个字符不能映射到同一个字符，但是字符可以映射到其本身。
#
# 测试样例如题目描述。
#
# 可以假设s和t等长。
#
# 解题思路：
# 使用两个哈希表sourceMap和targetMap维护两个字符串中字符的映射关系。
#
# sourceMap[ t[x] ] = s[x]
#
# targetMap[ s[x] ] = t[x]
#
# 当出现映射不一致的情形时，返回False
#
# 否则返回True


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        sourceMap, targetMap = dict(), dict()
        for i in range(len(s)):
            source, target = sourceMap.get(t[i]), targetMap.get(s[i])
            if source is None and target is None:
                sourceMap[t[i]], targetMap[s[i]] = s[i], t[i]
            elif source != s[i] or target != t[i]:
                return False
        return True
