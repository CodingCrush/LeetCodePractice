class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        origin = bin(int(n))[2:]
        origin = '0' * (32 - len(origin)) + origin
        return int(origin[::-1], base=2)
