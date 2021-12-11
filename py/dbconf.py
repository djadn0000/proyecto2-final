import pymysql

class DataBase:
    def __init__(self) :
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Adrian00_@',
            db='Proyecto'
        )
        self.cursor =self.connection.cursor()

database = DataBase()
