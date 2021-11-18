from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks = sorted(tasks)
        workers = sorted(workers)

        def check(k):
            W = SortedList(workers[-k:])
            tries = pills

            for elem in tasks[:k][::-1]:
                place = W.bisect_left(elem)
                if place < len(W):
                    W.pop(place)
                elif tries > 0:
                    place2 = W.bisect_left(elem - strength)
                    if place2 < len(W):
                        W.pop(place2)
                        tries -= 1
                    else:
                        return False
                else:
                    return False

            return True

        lo, hi = 0, min(len(workers), len(tasks))
        while lo <= hi:
            mid = (lo + hi)//2
            if check(mid):
                lo = mid+1
            else:
                hi = mid-1

        return hi