# Time:  O(n^2)
# Space: O(n)
#
# Given a string s and a dictionary of words dict, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# 
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# 
# Return true because "leetcode" can be segmented as "leet code".
#
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(len(s) + 1)]
        
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]
if __name__ == "__main__":
    print Solution().wordBreak("leetcode", ["leet", "code"])
