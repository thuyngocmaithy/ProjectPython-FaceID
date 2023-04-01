
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from .BuoiHoc import BuoiHoc
from .ConnectDatabase import ConnectDatabase
import re

class BuoiHocDAL:

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
            cursor.execute("SELECT * FROM buoihoc")      
            for row in BuoiHocDAL.iter_row(cursor, 10):
                list.append(row)
        except Exception as e:
            print(e)
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list
    
    def countAll():
        count = 0
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM buoihoc")   
            row = cursor.fetchone()         
            if row is not None:
                count = row[0]
        except Exception as e:
            print(e)
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return count
    
    def generateID():
        ma = ""
        stt = ""
        try:
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            query = "SELECT `mabuoihoc` "\
                    + "FROM `buoihoc` "\
                    + "ORDER BY `mabuoihoc` DESC "\
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
        ma = "BH{0:03}".format(stt)
        return ma


    def add( bh: BuoiHoc):
        query = "INSERT INTO buoihoc (mabuoihoc, giobatdau, gioketthuc, ngay, malop, magiangvien)"\
                "VALUES(%s, %s, %s, %s, %s, %s)"
        data = (bh._mabuoihoc, bh._giobatdau,
                bh._gioketthuc, bh._ngay, bh._malop, bh._magiangvien)              
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

    def update( bh: BuoiHoc):
       # Câu lệnh update dữ liệu
        query = """ UPDATE buoihoc
                    SET giobatdau = %s,
                    gioketthuc = %s,
                    ngay = %s,
                    malop = %s,
                    magiangvien = %s
                    WHERE mabuoihoc = %s """

        data = (bh._giobatdau, bh._gioketthuc, bh._ngay,
                bh._malop, bh._magiangvien, bh._mabuoihoc)

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
        query = "DELETE FROM buoihoc WHERE mabuoihoc = '{}'".format(id)
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
        query = "SELECT * FROM buoihoc WHERE {} LIKE '%{}%'".format(key, value)
        try:
             # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query)
            for row in BuoiHocDAL.iter_row(cursor, 10):
                list.append(row)            
        except Exception as ex:
            print(ex)
    
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list
    def findMaBuoiHoc(value):
        list = []
        query = "SELECT * FROM buoihoc WHERE mabuoihoc = '{}'".format(value)
        try:
             # Kết nối database
            connDb = ConnectDatabase()
            conn = connDb.Connect()
            cursor = conn.cursor()
            cursor.execute(query)
            for row in BuoiHocDAL.iter_row(cursor, 10):
                list.append(row)            
        except Exception as ex:
            print(ex)
    
        finally:
            # Đóng kết nối
            cursor.close()
            conn.close()
        return list

