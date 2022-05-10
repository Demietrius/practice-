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
        try:
            self.databaseConnection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.databaseCursor = self.databaseConnection.cursor()
        except Exception as e:
            print(e)

    def create(self, request):
        data = (request["firstName"],
                request["lastName"],
                request["salary"],
                request["sex"],
                request["worksFor"])
        DatabaseAccessor.db_connection(self)
        cursor = self.databaseCursor
        sql = ("INSERT INTO Users (First_Name, Last_Name, Salary, Sex, Works_For)"
               "VALUES (%s, %s, %s, %s, %s) RETURN *")
        cursor.execute(sql, data)
        self.databaseConnection.commit()
        create_results = cursor.fetchall()
        print(f"New User Added: {create_results}")
        print("Updated Table")
        print("********************")
        self.user_table_print()

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
        self.user_table_print()

    def read(self, request):
        DatabaseAccessor.db_connection(self)
        cursor = self.databaseCursor
        data = (request,)
        sql = "SELECT * FROM Users WHERE User_ID = %s"
        cursor.execute(sql, data)
        read_results = cursor.fetchall()
        print(f"User Info: {read_results}")

    def delete(self, request):
        DatabaseAccessor.db_connection(self)
        cursor = self.databaseCursor
        data = (request,)
        sql = "DELETE FROM Users WHERE User_ID = %s"
        cursor.execute(sql, data)
        delete_results = cursor.fetchall()
        print(delete_results)
        self.user_table_print()

    def user_table_print(self):
        cursor = self.databaseCursor
        cursor.execute("SELECT * FROM Users")
        for x in cursor:
            print(x)
