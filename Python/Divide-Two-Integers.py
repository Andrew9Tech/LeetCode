# Time:  O(logn)
# Space: O(1)
# 
# Divide two integers without using multiplication, division and mod operator.
#

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        result, dvd, dvs = 0, abs(dividend), abs(divisor)
        while dvd >= dvs:
            i = 0; dvsTemp = dvs
            while dvd >= dvsTemp:
                i += 1
                dvsTemp = dvsTemp << 1
            dvd -= (dvsTemp >> 1)
            result += 1 << i - 1
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            if result >= 2147483648: return 2147483647
            else: return result
        else:
            return -result
        
if __name__ == "__main__":
    print Solution().divide(123, 12)
    print Solution().divide(123, -12)
    print Solution().divide(-123, 12)
    print Solution().divide(-123, -12)
