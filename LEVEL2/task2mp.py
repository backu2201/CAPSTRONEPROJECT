#multi-processing
from time import perf_counter,sleep
import os
import multiprocessing as mp
class Search:
    def task(self,file,drives):
        a=False
        sleep(1)
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
    p1=mp.Process(target=s.task,args=("f1.txt","d:\\"))
    p2=mp.Process(target=s.task,args=("f1.txt","c:\\hcl_programs"))
    start_time=perf_counter()
    p1.start()
    p2.start()
    end_time=perf_counter()
    print(f'{end_time - start_time}seconds')