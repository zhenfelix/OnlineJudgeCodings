class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

作者：力扣官方题解
链接：https://leetcode.cn/problems/search-in-rotated-sorted-array/solutions/220083/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            m = (left+right)//2
            if nums[m] >= nums[0]:
                left = m+1
            else:
                right = m-1
        p = right
        # print(p)
        idx = bisect_left(nums,target,0,p+1)
        # print(idx)
        if idx <= p and nums[idx] == target:
            return idx 
        idx = bisect_left(nums,target,p+1,n)
        # print(idx)
        if idx < n and nums[idx] == target:
            return idx
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        right += n
        while left <= right:
            mid = (left+right)//2
            if nums[mid%n] == target:
                return mid%n 
            elif nums[mid%n] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1