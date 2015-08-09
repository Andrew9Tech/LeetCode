# Time:  O(logn)
# Space: O(logn)
# 
# Implement pow(x, n).
#

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n < 0:
            return 1 / self.powRecu(x, -n)
        return self.powRecu(x, n)
    
    def powRecu(self, x, n):
        if n == 0:
            return 1.0
        N, result = n, 1.0
        while N:
            if N%2 == 0:
                N, x = N/2, x*x
            else:
                N, x, result = N/2, x*x, x*result
        return result

if __name__ == "__main__":
    print Solution().pow(3, 2)
    print Solution().pow(3,-2)
