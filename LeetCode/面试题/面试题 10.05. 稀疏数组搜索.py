class Solution:
    def findString(self, words: List[str], s: str) -> int:
        n = len(words)
        lo, hi = 0, n-1
        while lo <= hi:
            mid = (lo+hi)//2
            if words[mid] == s:
                return mid
            mid_ = mid 
            while mid_ <= hi and words[mid_] == '':
                mid_ += 1
            if mid_ > hi:
                hi = mid - 1
                continue
            if words[mid_] == s:
                return mid_
            elif words[mid_] < s:
                lo = mid_ + 1
            else:
                hi = mid - 1

        return -1