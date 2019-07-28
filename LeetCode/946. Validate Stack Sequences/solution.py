class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        idx, n = 0, len(popped)
        for p in pushed:
            st.append(p)
            while idx < n and len(st) > 0 and st[-1] == popped[idx]:
                st.pop()
                idx += 1
        return len(st) == 0