import mysql.connector
class ConnectDatabase:
    def Connect(self):            
        try:
            # Ket noi MySQL voi Python bang ham mysql.connector.connect()
            mydb = mysql.connector.connect(
                host="localhost", 
                user="root",
                password="",
                database="quanlysinhvien"
            )
        except: 
            print("Error connect!")
        return mydb