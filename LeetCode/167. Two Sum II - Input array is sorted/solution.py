class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                j-=1
        return []
    
    
# # two-pointer
# def twoSum1(self, numbers, target):
#     l, r = 0, len(numbers)-1
#     while l < r:
#         s = numbers[l] + numbers[r]
#         if s == target:
#             return [l+1, r+1]
#         elif s < target:
#             l += 1
#         else:
#             r -= 1
 
# # dictionary           
# def twoSum2(self, numbers, target):
#     dic = {}
#     for i, num in enumerate(numbers):
#         if target-num in dic:
#             return [dic[target-num]+1, i+1]
#         dic[num] = i