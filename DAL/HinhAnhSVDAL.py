
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from .HinhAnhSV import HinhAnhSV
from .ConnectDatabase import ConnectDatabase
import re

class HinhAnhSVDAL:

    def iter_row(cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row
    def get():
        list = []
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM hinhanh_sinhvien")            
            for row in HinhAnhSVDAL.iter_row(cursor, 10):
                list.append(row)
        except Exception as e:
            print(e)
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list    

    def add( ha_sv : HinhAnhSV):
        query = "INSERT INTO hinhanh_sinhvien "\
                "VALUES(%s, %s)"
        data = (ha_sv._masinhvien , ha_sv._hinhanh)              
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query, data)         
            if cursor.rowcount>0:
                conn.commit()
                return True
            
        except Exception as ex:
            print(ex)
            return False

        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return False
  
    def delete(id):
        query = "DELETE FROM hinhanh_sinhvien WHERE masinhvien = '{}'".format(id)
        try:
             # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query)
            if cursor.rowcount>0:
                conn.commit()
                return True
            
        except Exception as ex:
            print(ex)
            return False
    
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return False    
    def find(value):
        list = []
        query = "SELECT * FROM hinhanh_sinhvien WHERE masinhvien = '{}' LIMIT 1".format(value)
        try:
             # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query)
            for row in HinhAnhSVDAL.iter_row(cursor, 1):
                list.append(row)            
        except Exception as ex:
            print(ex)
    
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list