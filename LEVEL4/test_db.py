#test cases
import pytest
from drivessearch import Searchdrives
from task5_searcher import FileSearcher
class Test_Drive:
# test case for listing of all the drives in OS
    def test_DriveCase(self):
        obj=Searchdrives()
        self.expected=obj.getdrives()
        self.actual=['C:\\','D:\\']
        assert self.expected==self.actual
# test case for existence of the  given file
    def test_searchfile(self):
        obj=FileSearcher()
        d=obj.search_for_file('c','f1.txt')
        self.expected_file_name=d[0]
        self.actual_res='c:\hcl_programs\\f1.txt'
        assert self.expected_file_name == self.actual_res