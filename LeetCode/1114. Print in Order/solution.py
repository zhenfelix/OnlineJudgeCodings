# class Foo:
#     def __init__(self):
#         self.a, self.b, self.c = False, False, False


#     def first(self, printFirst: 'Callable[[], None]') -> None:
        
#         # printFirst() outputs "first". Do not change or remove this line.
#         printFirst()
#         self.a = True


#     def second(self, printSecond: 'Callable[[], None]') -> None:
        
#         # printSecond() outputs "second". Do not change or remove this line.
#         while not self.a:
#             pass
#         printSecond()
#         self.b = True


#     def third(self, printThird: 'Callable[[], None]') -> None:
        
#         # printThird() outputs "third". Do not change or remove this line.
#         while not self.b:
#             pass
#         printThird()
#         self.c = True
        
        
# from threading import Lock

# class Foo:
#     def __init__(self):
#         self.locks = (Lock(),Lock())
#         self.locks[0].acquire()
#         self.locks[1].acquire()
        
#     def first(self, printFirst):
#         printFirst()
#         self.locks[0].release()
        
#     def second(self, printSecond):
#         with self.locks[0]:
#             printSecond()
#             self.locks[1].release()
            
            
#     def third(self, printThird):
#         with self.locks[1]:
#             printThird()
            

# from threading import Event

# class Foo:
#     def __init__(self):
#         self.done = (Event(),Event())
        
#     def first(self, printFirst):
#         printFirst()
#         self.done[0].set()
        
#     def second(self, printSecond):
#         self.done[0].wait()
#         printSecond()
#         self.done[1].set()
            
#     def third(self, printThird):
#         self.done[1].wait()
#         printThird()

        
from threading import Semaphore

class Foo:
    def __init__(self):
        self.gates = (Semaphore(0),Semaphore(0))
        
    def first(self, printFirst):
        printFirst()
        self.gates[0].release()
        
    def second(self, printSecond):
        with self.gates[0]:
            printSecond()
            self.gates[1].release()
            
    def third(self, printThird):
        with self.gates[1]:
            printThird()
