# class Solution(object):
#     def validUtf8(self, data):
#         """
#         :type data: List[int]
#         :rtype: bool
#         """
#         idx = 0
#         while idx < len(data):
#             cur = data[idx]
#             if cur & (1<<7) == 0:
#                 cnt = 1
#             elif cur & (1<<7) > 0 and cur & (1<<6) > 0 and cur & (1<<5) == 0:
#                 cnt = 2
#             elif cur & (1<<7) > 0 and cur & (1<<6) > 0 and cur & (1<<5) > 0 and cur & (1<<4) == 0:
#                 cnt = 3
#             elif cur & (1<<7) > 0 and cur & (1<<6) > 0 and cur & (1<<5) > 0 and cur & (1<<4) > 0 and cur & (1<<3) == 0:
#                 cnt = 4
#             else:
#                 cnt = 0
#             # print(cnt)
#             if cnt == 0:
#                 return False
#             for i in range(cnt-1):
#                 idx += 1
#                 if idx >= len(data):
#                     return False
#                 cur = data[idx]
#                 if cur & (1<<7) > 0 and cur & (1<<6) == 0:
#                     continue
#                 return False
#             idx += 1
#         return True


class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        # Number of bytes in the current UTF-8 character
        n_bytes = 0

        # Mask to check if the most significant bit (8th bit from the left) is set or not
        mask1 = 1 << 7

        # Mask to check if the second most significant bit is set or not
        mask2 = 1 << 6
        for num in data:

            # Get the number of set most significant bits in the byte if
            # this is the starting byte of an UTF-8 character.
            mask = 1 << 7
            if n_bytes == 0:
                while mask & num:
                    n_bytes += 1
                    mask = mask >> 1

                # 1 byte characters
                if n_bytes == 0:
                    continue

                # Invalid scenarios according to the rules of the problem.
                if n_bytes == 1 or n_bytes > 4:
                    return False
            else:

                # If this byte is a part of an existing UTF-8 character, then we
                # simply have to look at the two most significant bits and we make
                # use of the masks we defined before.
                if not (num & mask1 and not (num & mask2)):
                    return False
            n_bytes -= 1
        return n_bytes == 0     
        