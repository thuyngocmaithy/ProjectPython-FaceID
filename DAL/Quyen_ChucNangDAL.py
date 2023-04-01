
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from .Quyen_ChucNang import Quyen_ChucNang
from .ConnectDatabase import ConnectDatabase
import re

class Quyen_ChucNangDAL:

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
            cursor.execute("SELECT * FROM quyen_chucnang")            
            for row in Quyen_ChucNangDAL.iter_row(cursor, 10):
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
            query = "SELECT `maquyen_chucnang` "\
                    + "FROM `quyen_chucnang` "\
                    + "ORDER BY `maquyen_chucnang` DESC "\
                    + "LIMIT 1"
            cursor.execute(query)
            row = cursor.fetchone()
            if (row is None and cursor.rowcount == -1):
                stt = "0"
            else:
                stt = row[0]
        except:
            print("Lỗi tăng id")
        stt = (int)(re.sub("[^0-9]", "",stt))+1
        ma = "GV{0:03}".format(stt)
        return ma


    def add( qcn: Quyen_ChucNang):
        query = "INSERT INTO quyen_chucnang "\
                "VALUES(%s, %s)"
        data = (qcn._maquyen, qcn._machucnang)              
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

    def update( qcn: Quyen_ChucNang):
       # Câu lệnh update dữ liệu
        query = """ UPDATE quyen_chucnang
                    SET machucnang = %s
                    WHERE maquyen = %s 
                    AND machucnang = %s """

        data = (qcn._machucnang, qcn._maquyen, qcn._machucnang)

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
    def delete(maquyen):
        query = "DELETE FROM quyen_chucnang WHERE maquyen = '{}'".format(maquyen)
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
    def getListChucNangTheoQuyen(maquyen):
        list = []
        query = """ SELECT machucnang
                    FROM quyen_chucnang
                    WHERE maquyen = '{}' """.format(maquyen)
        try:
            # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query)
            for row in Quyen_ChucNangDAL.iter_row(cursor, 10):
                list.append(row[0])
            
        except Exception as ex:
            print(ex)            
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list
    # def find(key, value):
    #     list = []
    #     query = "SELECT * FROM quyen_chucnang WHERE {} LIKE '%{}%'".format(key, value)
    #     try:
    #          # Kết nối database
    #         connDb = ConnectDatabase()
    #         conn = connDb.Connect()
    #         cursor = conn.cursor()
    #         cursor.execute(query)
    #         for row in Quyen_ChucNangDAL.iter_row(cursor, 10):
    #             list.append(row)            
    #     except Exception as ex:
    #         print(ex)
    
    #     finally:
    #         # Đóng kết nối
    #         cursor.close()
    #         conn.close()
    #     return list
    

    

