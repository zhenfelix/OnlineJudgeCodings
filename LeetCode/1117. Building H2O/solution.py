# Since collections.deque is thread-safe, so we can do it this way:


# from collections import deque
# class H2O:
#     def __init__(self):
#         self._hq, self._oq = deque(), deque()

#     def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
#         self._hq.append(releaseHydrogen)
#         self._check()

#     def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
#         self._oq.append(releaseOxygen)
#         self._check()
        
#     def _check(self) -> None:
#         if len(self._hq) > 1 and len(self._oq) > 0:
#             self._hq.popleft()()
#             self._hq.popleft()()
#             self._oq.popleft()()

from threading import Lock

class H2O(object):
    def __init__(self):
        self.H = 0
        self.O = 0
        self.mu = Lock()
        pass


    def hydrogen(self, releaseHydrogen):
        self.releaseHydrogen = releaseHydrogen
        with self.mu:
            self.H += 1
            self.ouput()

    def oxygen(self, releaseOxygen):
        self.releaseOxygen = releaseOxygen
        with self.mu:
            self.O += 1
            self.ouput()
        
    def ouput(self):
        while self.ok():
            self.releaseHydrogen()
            self.releaseHydrogen()
            self.releaseOxygen()
            self.H -= 2
            self.O -= 1
    
    def ok(self):
        return self.H >= 2 and self.O >= 1