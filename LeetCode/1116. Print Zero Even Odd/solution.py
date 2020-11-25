# from threading import Semaphore
# class ZeroEvenOdd:
#     def __init__(self, n):
#         self.n = n
#         self.sem0, self.sem1, self.sem2 = Semaphore(1), Semaphore(0), Semaphore(0)
        
        
#     # printNumber(x) outputs "x", where x is an integer.
#     def zero(self, printNumber: 'Callable[[int], None]') -> None:
#         for i in range(1,self.n+1):
#             self.sem0.acquire()
#             printNumber(0)
#             if i&1 == 1:
#                 self.sem1.release()
#             else:
#                 self.sem2.release()

        
        
#     def even(self, printNumber: 'Callable[[int], None]') -> None:
#         for i in range(1,self.n+1):
#             if i&1 == 0:
#                 self.sem2.acquire()
#                 printNumber(i)
#                 self.sem0.release()
        
        
        
#     def odd(self, printNumber: 'Callable[[int], None]') -> None:
#         for i in range(1,self.n+1):
#             if i&1 == 1:
#                 self.sem1.acquire()
#                 printNumber(i)
#                 self.sem0.release()
        
from threading import Condition
import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cv = Condition()
        self.cur = 1
        self.printZero = True

    # printNumber(x) outputs "x", where x is an integer.

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.cur <= self.n:
            with self.cv:
                while not self.printZero:
                    self.cv.wait()
                if self.cur <= self.n:
                    printNumber(0)
                self.printZero = not self.printZero
                self.cv.notify_all()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while self.cur <= self.n:
            with self.cv:
                while self.printZero or self.cur & 1 == 1:
                    self.cv.wait()
                if self.cur <= self.n:
                    printNumber(self.cur)
                    self.cur += 1
                self.printZero = not self.printZero
                self.cv.notify_all()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while self.cur <= self.n:
            with self.cv:
                while self.printZero or self.cur & 1 == 0:
                    self.cv.wait()
                if self.cur <= self.n:
                    printNumber(self.cur)
                    self.cur += 1
                self.printZero = not self.printZero
                self.cv.notify_all()