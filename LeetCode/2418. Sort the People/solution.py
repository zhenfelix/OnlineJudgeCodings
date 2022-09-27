class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = [(h,n) for h,n in zip(heights,names)]
        ans = []
        for h,n in sorted(arr, reverse=True):
            ans.append(n)
        return ans