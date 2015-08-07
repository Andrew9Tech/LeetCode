#
# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
#

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        Dict = {}
        for item in s:
            if item not in Dict:   Dict[item] = 1
            else:   Dict[item] += 1
        for item in t:
            if item not in Dict:    return False
            elif Dict[item] > 1:   Dict[item] -= 1
            else:   del Dict[item]
        if Dict == {}:
            return True
        else:
            return False
            
            
 class Solution2:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)  
  
  #推荐此种方法，Counter类是字典子类，Counter类的目的是用来跟踪值出现的次数。
  #它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）
  class Solution3:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        from collections import Counter
        return Counter(s).items() == Counter(t).items()          
            
if __name__ == "__main__":
    s = str("rat")
    t = str("car")
    print Solution().isAnagram(s, t)
