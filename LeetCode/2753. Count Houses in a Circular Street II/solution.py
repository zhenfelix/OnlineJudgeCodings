# # Definition for a street.
# # class Street:
# #     def closeDoor(self):
# #         pass
# #     def isDoorOpen(self):
# #         pass
# #     def moveRight(self):
# #         pass
# class Solution:
#     def houseCount(self, street: Optional['Street'], k: int) -> int:
#         while not street.isDoorOpen():
#             street.moveRight()
#         cnt = delta = 0
#         street.moveRight()
#         while delta <= k:
#             while delta <= k and not street.isDoorOpen():
#                 delta += 1
#                 street.moveRight()
#             street.closeDoor()
#             delta += 1
#             street.moveRight()
#             if delta <= k:
#                 cnt += delta
#                 delta = 0
#         return cnt 

class Solution:

    def houseCount(self, s: Optional['Street'], k: int) -> int:

        while not s.isDoorOpen():

            s.moveRight()

        for i in range(1, k + 1):

            s.moveRight()

            if s.isDoorOpen():

                ans = i

                s.closeDoor()

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/count-houses-in-a-circular-street-ii/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。