import mysql.connector


class DatabaseAccessor:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.databaseConnection = None
        self.databaseCursor = None

    def db_connection(self):
        self.databaseConnection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.databaseCursor = self.databaseConnection.cursor()

    def create(self, request):
        data = (request["firstName"], request["lastName"], request["salary"],
                request["sex"], request["worksFor"])
        DatabaseAccessor.db_connection(self)
        cursor = self.databaseCursor
        sql = ("INSERT INTO Users (First_Name, Last_Name, Salary, Sex, Works_For)"
               "VALUES (%s, %s, %s, %s, %s)")
        cursor.execute(sql, data)
        self.databaseConnection.commit()
        self.table_print(cursor)

    def update(self, request):
        data = (request["firstName"],
                request["lastName"],
                request["salary"],
                request["sex"],
                request["worksFor"],
                request["userID"])
        DatabaseAccessor.db_connection(self)
        cursor = self.databaseCursor
        sql = ("UPDATE Users SET First_Name = %s, Last_Name = %s, Salary = %s,"
               "Sex = %s, Works_For = %s WHERE User_ID = %s")
        cursor.execute(sql, data)
        self.databaseConnection.commit()
        self.table_print(cursor)

    def read(self, request):
        DatabaseAccessor.db_connection(self)
        cursor = self.databaseCursor
        data = (request,)
        sql = "SELECT * FROM Users WHERE User_ID = %s"
        cursor.execute(sql, data)
        read_results = cursor.fetchall()
        print(read_results)
        self.table_print(cursor)

    def delete(self, request):
        DatabaseAccessor.db_connection(self)
        cursor = self.databaseCursor
        data = (request,)
        sql = "DELETE FROM Users WHERE User_ID = %s"
        cursor.execute(sql, data)
        delete_results = cursor.fetchall()
        print(delete_results)
        self.table_print(cursor)

    @staticmethod
    def table_print(cursor):
        cursor.execute("SELECT * FROM Users")
        for x in cursor:
            print(x)
