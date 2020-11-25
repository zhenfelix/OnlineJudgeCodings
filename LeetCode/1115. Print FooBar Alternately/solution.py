from threading import Semaphore
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_sem = Semaphore()
        self.bar_sem = Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.foo_sem.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_sem.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.bar_sem.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_sem.release()



# import threading

# from threading import Semaphore
# class FooBar:
#     def __init__(self, n):
#         self.n = n
#         self.foo_sem = Semaphore()
#         self.bar_sem = Semaphore(0)

#     def foo(self, printFoo: 'Callable[[], None]') -> None:

#         for i in range(self.n//2):
#             # very important otherwise deadlock
#             self.foo_sem.acquire()
#             # printFoo() outputs "foo". Do not change or remove this line.
#             printFoo()
#             self.bar_sem.release()

#     def bar(self, printBar: 'Callable[[], None]') -> None:

#         for i in range(self.n):
#             self.bar_sem.acquire()
#             # printBar() outputs "bar". Do not change or remove this line.
#             printBar()
#             self.foo_sem.release()


# if __name__ == "__main__":
#     FB = FooBar(100)
#     def printFoo():
#         print("1", end='')
#     def printBar():
#         print("0", end='')
#     f, b = threading.Thread(target=FB.foo, args=(printFoo,)), threading.Thread(
#         target=FB.bar, args=(printBar,))
#     f2 = threading.Thread(target=FB.foo, args=(printFoo,))
#     f.start()
#     b.start()
#     f2.start()
#     f.join()
#     b.join()
#     f2.join()
#     print("Done")
