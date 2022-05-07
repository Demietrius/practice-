import mysql.connector

class DBAccess:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database


class Business:

    def __init__(self, business_id, business_name, business_type, number_of_employees):
        self.business_id = int(business_id),
        self.business_name = business_name,
        self.business_type = business_type,
        self.number_of_employees = int(number_of_employees)


class User:

    def __init__(self, first_name, last_name, salary, sex, works_for):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.sex = sex
        self.works_for = works_for


    def insert_user(self, database):
        db = mysql.connector.connect(
            host=database.host,
            user=database.user,
            password=database.password,
            database=database.database
        )
        mycursor = db.cursor()
        b_data = (self.first_name, self.last_name,
                  self.salary, self.sex, self.works_for)
        b_insert = ("INSERT INTO Users (First_Name, Last_Name, Salary, Sex, Works_For)"
                    "VALUES (%s, %s, %s, %s, %s) RETURN *")
        mycursor.execute(b_insert, b_data)
        db.commit()



