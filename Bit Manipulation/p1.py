class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        result = 0
        for bit in range(32):
            result <<= 1
            result |= A & 1
            A >>= 1
        return result


a=Solution()
print(a.reverse(1))