# multi-threading
from time import perf_counter,sleep
from threading import Thread
import os
class Search:
    def task(self,file,drives):
        a=False
        #sleep(1)
        for r, d, f in os.walk(drives):
            for j in f:
                if j == file:
                    a=True
                    break
        if a:
            print("file is found in {}".format(drives))
        else:
            print("file is not found in {}".format(drives))
if __name__ == "__main__":
    s=Search()
    t1 = Thread(target=s.task, args=("f1.txt", "d:\\"))
    t2 = Thread(target=s.task, args=("f1.txt", "c:\\hcl_programs"))
    start_time = perf_counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = perf_counter()
    print(f'{end_time - start_time}seconds')