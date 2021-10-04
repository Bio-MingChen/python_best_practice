import time
import random
from collections import namedtuple
from threading import Thread,Semaphore,current_thread,Lock

def thread_enhance(thread=None):
    """
    A decorator to provide semaphore and exception handle function
    for mutiple threading 
    ------------------------
    thread: number of thread [integer]
    """
    sema = Semaphore(thread) if thread else None

    def decorator(func):
        def wrapper(*args,**kwargs):

            class TH(Thread):
                def __init__(self):
                    super().__init__()
                    self.error = 0
                    self.msg = "ok"

                def run(self):
                    if sema:
                        sema.acquire()
                    try:
                        func(*args,**kwargs)
                    except Exception as e:
                        pass
                        print("exception happened!")
                        # print(e)
                        self.error = 1
                        self.msg = e
                    if sema:
                        sema.release()
            return TH()            
        return wrapper
    return decorator

@thread_enhance()
def func():
    print(f"Current threading:{current_thread().name}")
    print("start run ...")
    print(1/0)


@thread_enhance(3)
def run():
    print(f"Current threading:{current_thread().name}")
    print("start run ...")
    time.sleep(random.randint(1,3))
    print("end run...")

#==========================test function ================

def func_test():
    th = func()
    th.start()
    th.join()

    # print(dir(th))
    if th.error != 0:
        print(th.msg)
    else:
        print("No error in thread")
    print("main thread end.")

def muti_thread_func(func):
    ths = []
    for _ in range(100):
        th = func()
        th.start()
        ths.append(th)
    
    for th in ths:
        th.join()


lock = Lock()

@thread_enhance(3)
def write_func():
    with lock:
        with open("lock_example.txt",'a+') as odata:
            odata.write("Write something...\n")

@thread_enhance(30)
def write_nolock_func():
    with open("lock_example.txt",'a+') as odata:
        odata.write("Write something...\n")

if __name__ == "__main__":
    # func_test()
    # muti_thread_func(run)
    # muti_thread_func(write_func)
    muti_thread_func(write_nolock_func)
