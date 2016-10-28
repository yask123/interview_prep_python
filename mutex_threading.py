import threading
import time
import random

lock = threading.Lock()

class MyThread1(threading.Thread):
    def run(self):
        global lock
        print 'Thread1 is sleeping'
        time.sleep(random.randint(1,10))
        print 'I should finish first'
        lock.release()

class MyThread2(threading.Thread):
    def run(self):
        global lock
        print 'Thread2 is sleeping'
        time.sleep(random.randint(1,10))
        lock.acquire()
        print 'I should finish last'

lock.acquire()
m1 = MyThread1()
m2 = MyThread2()

m1.start()
m2.start()
