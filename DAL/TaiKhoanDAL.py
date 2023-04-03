
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from .TaiKhoan import TaiKhoan
from .ConnectDatabase import ConnectDatabase
import re

class TaiKhoanDAL:

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
            cursor.execute("SELECT * FROM taikhoan")            
            for row in TaiKhoanDAL.iter_row(cursor, 10):
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
            query = "SELECT `mataikhoan` "\
                    + "FROM `taikhoan` "\
                    + "ORDER BY `mataikhoan` DESC "\
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
        ma = "TK{0:03}".format(stt)
        return ma


    def add( tk: TaiKhoan):
        query = "INSERT INTO taikhoan "\
                "VALUES(%s, %s, %s, %s)"
        data = (tk._mataikhoan, tk._email, tk._matkhau,tk._maquyen)   
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

    def update( tk: TaiKhoan):
       # Câu lệnh update dữ liệu
        query = """ UPDATE taikhoan
                    SET email = %s,
                    maquyen = %s
                    WHERE mataikhoan = %s """

        data = (tk._email, tk._maquyen, tk._mataikhoan)
        
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
        query = "DELETE FROM taikhoan WHERE mataikhoan = '{}'".format(id)
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
        query = "SELECT * FROM taikhoan WHERE {} LIKE '%{}%'".format(key, value)
        try:
             # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query)
            for row in TaiKhoanDAL.iter_row(cursor, 10):
                list.append(row)            
        except Exception as ex:
            print(ex)
    
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list

    def checkLogin(email,password):
        global cursor
        query = 'SELECT * FROM `taikhoan` WHERE `email` = %s and `matkhau` = %s'
        try:
             # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            vals = (email, password)        
            cursor.execute(query, vals)
            user = cursor.fetchone()
            if user is not None:                
                return user[1], user[2], user[3]
        except Exception as ex:
            print(ex)
    
        finally:
            # Đóng kết nối
            
            cursor.close()
            conn.close()
        return False

    def changePassword(email, mkmoi):
        # Câu lệnh update dữ liệu
        query = """ UPDATE taikhoan
                    SET matkhau = %s
                    WHERE email = %s """

        data = (mkmoi, email)
        
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
    def checkNotTaiKhoanAmin(mataikhoan):
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            query = """
            SELECT *
            FROM taikhoan
            WHERE mataikhoan = '{}'
            AND maquyen = 'Q001' """.format(mataikhoan)
            cursor.execute(query)
            row = cursor.fetchone()
            if (row is None and cursor.rowcount == -1):
                return True
        except Exception as ex:
            print(ex)
        return False