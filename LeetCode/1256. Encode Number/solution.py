class Solution:
    # def encode(self, num: int) -> str:
    #     num += 1
    #     res = "{0:b}".format(num)
    #     return res[1:]

    def encode(self, n):
        return bin(n + 1)[3:]