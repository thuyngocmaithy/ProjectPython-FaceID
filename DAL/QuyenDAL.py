
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from .Quyen import Quyen
from .ConnectDatabase import ConnectDatabase
import re

class QuyenDAL:

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
            cursor.execute("SELECT * FROM quyen")            
            for row in QuyenDAL.iter_row(cursor, 10):
                list.append(row)
        except Exception as e:
            print(e)
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list

    def generateID():
        ma = ""
        stt = ""
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            query = "SELECT `maquyen` "\
                    + "FROM `quyen` "\
                    + "ORDER BY `maquyen` DESC "\
                    + "LIMIT 1"
            cursor.execute(query)
            row = cursor.fetchone()
            if (row is not None and cursor.rowcount == 0):
                stt = "0"
            else:
                stt = row[0]
        except:
            print("Lỗi tăng id")
        stt = (int)(re.sub("[^0-9]", "",stt))+1
        ma = "GV{0:03}".format(stt)
        return ma


    def add( q: Quyen):
        query = "INSERT INTO quyen "\
                "VALUES(%s, %s)"
        data = (q._maquyen, q._tenquyen)              
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

    def update( q: Quyen):
       # Câu lệnh update dữ liệu
        query = """ UPDATE quyen
                    SET tenquyen = %s
                    WHERE maquyen = %s """

        data = (q._tenquyen, q._maquyen)

        try:
            # Kết nối database
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
        query = "DELETE FROM quyen WHERE maquyen = '{}'".format(id)
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
    def find(key, value):
        list = []
        query = "SELECT * FROM quyen WHERE {} LIKE '%{}%'".format(key, value)
        try:
             # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query)
            for row in QuyenDAL.iter_row(cursor, 10):
                list.append(row)            
        except Exception as ex:
            print(ex)
    
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list
    

    

