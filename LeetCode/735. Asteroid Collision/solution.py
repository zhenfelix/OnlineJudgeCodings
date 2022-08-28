# class Solution:
#     def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         st = []
#         for a in asteroids:
#             same = False
#             while a < 0 and st and st[-1] > 0 and st[-1] < -a:
#                 st.pop()
#             if a < 0 and st and st[-1] == -a:
#                 st.pop()
#                 same = True
#             if same or (a < 0 and st and st[-1] > -a):
#                 continue
#             st.append(a)
#         return st 

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for aster in asteroids:
            alive = True
            while alive and aster < 0 and st and st[-1] > 0:
                alive = st[-1] < -aster
                if st[-1] <= -aster:
                    st.pop()
            if alive:
                st.append(aster)
        return st


# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/asteroid-collision/solution/xing-xing-peng-zhuang-by-leetcode-soluti-u3k0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。