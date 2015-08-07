
# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count, num = 0, n
        while num:
            count += 1
            num = (num - 1) & num
        return count
