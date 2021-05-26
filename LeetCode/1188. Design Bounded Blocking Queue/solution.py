from threading import Thread
from threading import Condition
from threading import current_thread
from threading import Lock
import time
import random


from threading import Condition


class BoundedBlockingQueue(object):

    def __init__(self, max_size):
        self.max_size = max_size
        self.curr_size = 0
        self.cond = Condition()
        self.q = []

    def dequeue(self):
        with self.cond:
            while self.curr_size == 0:
                self.cond.wait()
            item = self.q.pop(0)
            self.curr_size -= 1
            self.cond.notifyAll()

        return item

    def enqueue(self, item):
        with self.cond:
            while self.curr_size == self.max_size:
                self.cond.wait()
            self.q.append(item)
            self.curr_size += 1
            self.cond.notifyAll()
            # print("\ncurrent size of queue {0}".format(self.curr_size), flush=True)
    
    
    def size(self):
        return self.curr_size




def consumer_thread(q):
    while 1:
        item = q.dequeue()
        print("\n{0} consumed item {1}".format(current_thread().getName(), item), flush=True)
        time.sleep(random.randint(1, 3))


def producer_thread(q, val):
    item = val
    while 1:
        q.enqueue(item)
        item += 1
        time.sleep(0.1)


if __name__ == "__main__":
    blocking_q = BoundedBlockingQueue(5)

    consumerThread1 = Thread(target=consumer_thread, name="consumer-1", args=(blocking_q,), daemon=True)
    consumerThread2 = Thread(target=consumer_thread, name="consumer-2", args=(blocking_q,), daemon=True)
    producerThread1 = Thread(target=producer_thread, name="producer-1", args=(blocking_q, 1), daemon=True)
    producerThread2 = Thread(target=producer_thread, name="producer-2", args=(blocking_q, 100), daemon=True)

    consumerThread1.start()
    consumerThread2.start()
    producerThread1.start()
    producerThread2.start()

    time.sleep(15)
    print("Main thread exiting")