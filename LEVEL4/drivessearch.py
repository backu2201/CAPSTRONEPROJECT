#to display the list of drives present in the OS
import win32api
class Searchdrives:

    def getdrives(self):
        drives=win32api.GetLogicalDriveStrings()
        drives=drives.split('\000')[:-1]
        return drives
g=Searchdrives()
print(g.getdrives())

#Another way to find the list of drives
# class Searchdrives:
#     def find_drives(self):
#         print("this is the drives found: ")
#         drives=[]
#         for x in range(65,91):
#             if os.path.exists(chr(x)+":"):
#                 drives.append(chr(x))
#         return drives