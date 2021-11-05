class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        st = []
        nxt = [-1]*n
        mp = {v:i for i,v in enumerate(nums2)}
        for i in range(n)[::-1]:
            while st and st[-1] <= nums2[i]:
                st.pop()
            if st:
                nxt[i] = st[-1]
            st.append(nums2[i])
        ans = [-1]*len(nums1)
        for i, v in enumerate(nums1):
            ans[i] = nxt[mp[v]]
        return ans




class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        st = []
        nxt = [-1]*n
        mp = dict()
        for i, v in enumerate(nums2):
            while st and nums2[st[-1]] < v:
                nxt[st.pop()] = v
            st.append(i)
            mp[v] = i
        ans = [-1]*len(nums1)
        for i, v in enumerate(nums1):
            ans[i] = nxt[mp[v]]
        return ans
