# from threading import Lock
# class DiningPhilosophers:
#     def __init__(self):
#         self.locks = [Lock() for _ in range(5)]

#     # call the functions directly to execute, for example, eat()
#     def wantsToEat(self,
#                    philosopher: int,
#                    pickLeftFork: 'Callable[[], None]',
#                    pickRightFork: 'Callable[[], None]',
#                    eat: 'Callable[[], None]',
#                    putLeftFork: 'Callable[[], None]',
#                    putRightFork: 'Callable[[], None]') -> None:
#         left, right = philosopher, (philosopher-1)%5
#         if philosopher & 1:
#             self.locks[left].acquire()
#             pickLeftFork()
#             self.locks[right].acquire()
#             pickRightFork()
#             eat()
#             putRightFork()
#             self.locks[right].release()
#             putLeftFork()
#             self.locks[left].release()
#         else:
#             self.locks[right].acquire()
#             pickRightFork()
#             self.locks[left].acquire()
#             pickLeftFork()
#             eat()
#             putLeftFork()
#             self.locks[left].release()
#             putRightFork()
#             self.locks[right].release()

# from threading import Lock
# class DiningPhilosophers:
#     def __init__(self):
#         self.locks = [Lock() for _ in range(5)]

#     # call the functions directly to execute, for example, eat()
#     def wantsToEat(self, philosopher: int, pickLeftFork: 'Callable[[], None]',
#                    pickRightFork: 'Callable[[], None]',
#                    eat: 'Callable[[], None]',
#                    putLeftFork: 'Callable[[], None]',
#                    putRightFork: 'Callable[[], None]') -> None:
#         if philosopher != 0:
#             first, second = philosopher, (philosopher + 1) % 5
#         else:
#             second, first = philosopher, (philosopher + 1) % 5
#         with self.locks[first]:
#             with self.locks[second]:
#                 pickLeftFork()
#                 pickRightFork()
#                 eat()
#                 putLeftFork()
#                 putRightFork()


# from threading import Semaphore

# class DiningPhilosophers:
#     def __init__(self):
#         self.locks = [Semaphore(1) for _ in range(5)]

#     def wantsToEat(self, index, *actions):
#         left, right = index, (index - 1) % 5
        
#         if index:
#             with self.locks[left], self.locks[right]:
#                 for action in actions:
#                     action()
#         else:
#             with self.locks[right], self.locks[left]:
#                 for action in actions:
#                     action()


from threading import Semaphore

class DiningPhilosophers:
    def __init__(self):
        self.sizelock = Semaphore(4)
        # self.locks = [Lock() for _ in range(5)]
        self.locks = [Semaphore(1) for _ in range(5)]

    def wantsToEat(self, index, *actions):
        left, right = index, (index - 1) % 5
        with self.sizelock, self.locks[left], self.locks[right]:
            for action in actions:
                action()           