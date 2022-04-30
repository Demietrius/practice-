from db_access import DBAccess, User, Business
import mysql.connector

database = DBAccess('localhost', 'root', 'Ng13gHc##', 'user_business')

business_id = 20
business_name = 'Whataburger'
business_type = 'Food'
number_of_employees = 18

first_name = "Bobby"
last_name = "Witt"
salary = "700000"
sex = "M"
user_id = 22
works_for = 402

new_business = Business(business_id, business_name, business_type, number_of_employees)
new_user = User(first_name, last_name, salary, sex, user_id, works_for)


def insert_business(database, new_business):
    db = mysql.connector.connect(
        host=database.host,
        user=database.user,
        password=database.password,
        database=database.database
    )
    mycursor = db.cursor()
    b_data = (new_business.business_id[0], new_business.business_name[0],
              new_business.business_type[0], new_business.number_of_employees)
    b_insert = ("INSERT INTO Business (Business_ID, Business_Name, Business_Type, Number_Of_Employees)"
                "VALUES (%s, %s, %s, %s)")
    mycursor.execute(b_insert, b_data)
    mycursor.execute("SELECT * FROM Business")

    for x in mycursor:
        print(x)


def insert_user(database, new_user):
    db = mysql.connector.connect(
        host=database.host,
        user=database.user,
        password=database.password,
        database=database.database
    )
    mycursor = db.cursor()
    b_data = (new_user.first_name, new_user.last_name,
              new_user.salary, new_user.sex, new_user.user_id,
              new_user.works_for)
    b_insert = ("INSERT INTO Users (First_Name, Last_Name, Salary, Sex, User_ID, Works_For)"
                "VALUES (%s, %s, %s, %s, %s, %s)")
    mycursor.execute(b_insert, b_data)
    mycursor.execute("SELECT * FROM Users")

    for x in mycursor:
        print(x)

insert_business(database, new_business)
insert_user(database, new_user)








