from db_access import DBAccess, User, Business
import mysql.connector
import json


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
    db.commit()
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
    db.commit()
    mycursor.execute("SELECT * FROM Users")

    for x in mycursor:
        print(x)


with open("../src/db_login.json", "r") as f:
    db_login = json.load(f)

    database = DBAccess(db_login['login']['host'],
                        db_login['login']['user'],
                        db_login['login']['password'],
                        db_login['login']['database'])


with open("JSON_User_Update.json", "r") as f:
    user_list = json.load(f)

    for person in user_list['users']:
        new_user = User(person['first_name'],
                        person['last_name'],
                        person['salary'],
                        person['sex'],
                        person['user_id'],
                        person['works_for'])
        insert_user(database, new_user)

with open("../src/business_list.json", "r") as f:
    business_list = json.load(f)

    for person in business_list['business']:
        new_business = Business(person['business_id'],
                                person['business_name'],
                                person['business_type'],
                                person['number_of_employees'])
        insert_business(database, new_business)
