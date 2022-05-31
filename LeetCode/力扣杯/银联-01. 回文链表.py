# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        n = len(arr)
        # @lru_cache(None)
        def dfs(left, right, cnt):
            if cnt > 1:
                return False
            if left > right:
                return True
            if arr[left] != arr[right]:
                return dfs(left+1,right,cnt+1) or dfs(left,right-1,cnt+1)
            return dfs(left+1,right-1,cnt)
        return dfs(0,n-1,0)



class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = list()
        while head:
            nums.append(head.val)
            head = head.next

        left, right = 0, len(nums) - 1
        while left < right and nums[left] == nums[right]:
            left, right = left + 1, right - 1

        def check(left: int, right: int) -> bool:
            while left < right and nums[left] == nums[right]:
                left, right = left + 1, right - 1
            return left >= right

        return check(left + 1, right) or check(left, right - 1)


作者：🤪
链接：https://leetcode-cn.com/circle/discuss/YfxFdF/view/00gFZC/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。