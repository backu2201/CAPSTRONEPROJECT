# search for a file-path in all drives
import os
from drivessearch import Searchdrives
from time import perf_counter

class Search:
    def search_file(self,file,drives):
        file_exist=[]
        for i in drives:
            for r,d,f in os.walk(i):
                for j in f:
                    if j==file:
                        print("file is found in {}".format(i))
                        file_exist.append(i)
                        print(r)
                        break
        for i in range(len(drives)):
            if drives[i] not in file_exist:
                print("file not found in {}".format(drives[i]))

if __name__ == "__main__":
    file=input("Enter the file name to be searched: ")
    start_time = perf_counter()
    obj=Searchdrives()
    drives=obj.getdrives()
    s=Search()
    s.search_file(file,drives)
    end_time = perf_counter()
    print(end_time-start_time)
