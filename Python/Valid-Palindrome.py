# Time:  O(n)
# Space: O(1)
#
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# 
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# 
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
# 
# For the purpose of this problem, we define empty string as valid palindrome.
#

# s为字符串
# s.isalnum() 所有字符都是数字或者字母
# s.isalpha() 所有字符都是字母
# s.isdigit() 所有字符都是数字
# s.islower() 所有字符都是小写
# s.isupper() 所有字符都是大写
# s.istitle() 所有单词都是首字母大写，像标题
# s.isspace() 所有字符都是空白字符、\t、\n、\r


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True

if __name__ == "__main__":
    print Solution().isPalindrome("A man, a plan, a canal: Panama")
