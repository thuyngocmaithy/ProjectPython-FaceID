import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.HinhAnhSVDAL import HinhAnhSVDAL
from DAL.HinhAnhSV import HinhAnhSV

class HinhAnhSVBUS:
    def get(self):
        return HinhAnhSVDAL.get()
    def add(self, ha_sv:HinhAnhSV):
        return HinhAnhSVDAL.add(ha_sv)
    def delete(self, id):
        return HinhAnhSVDAL.delete(id)
    def find(self,value):
        return HinhAnhSVDAL.find(value)