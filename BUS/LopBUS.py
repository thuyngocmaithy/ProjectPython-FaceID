import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from DAL.LopDAL import LopDAL
from DAL.Lop import Lop

class LopBUS:
    def get(self):
        return LopDAL.get()