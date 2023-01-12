#logger file
import re
import logging
class searchLog():
    def _init_(self):
        logging.basicConfig(filename='filelog2.txt',level=logging.INFO)
    def searchlog(self,filename):
        file=open("filelog2.txt","r")
        str='team.txt'
        data=re.compile(str)
        res=data.search(str)
        line=file.readLine()
        print(res.group(0));

# if _name=='main_':
#     a=searchLog()
#     a.searchlog()