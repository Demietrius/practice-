import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ng13gHc##",
    database="user_business"
)

mycursor = db.cursor()


def business_insert():
    business_add = input("Would you like to add a business to the database? ")
    if business_add.lower() == 'yes':
        business_id = int(input("Enter Business ID: "))
        business_name = input("Enter Business Name: ")
        business_type = input("Enter Business Type: ")
        number_of_employees = int(input("Enter Number of Employees: "))
        b_data = (business_id, business_name, business_type, number_of_employees)
        b_insert = ("INSERT INTO Business (Business_ID, Business_Name, Business_Type, Number_Of_Employees)"
                    "VALUES (%s, %s, %s, %s)")
        mycursor.execute(b_insert, b_data)


def user_insert():
    user_add = input("Would you like to add a User to the database? ")
    if user_add.lower() == 'yes':
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        salary = int(input("Enter User Salary: "))
        sex = input("Enter User Sex (M/F): ")
        user_id = int(input("Enter User ID: "))
        works_for = int(input("Enter Business ID for Company where User is employed: "))
        u_data = (first_name, last_name, salary, sex, user_id, works_for)
        u_insert = ("INSERT INTO Users (First_Name, Last_name, Salary, Sex, User_ID, Works_For)"
                    "VALUES (%s, %s, %s, %s, %s, %s)")
        mycursor.execute(u_insert, u_data)

business_insert()


user_insert()

db.commit()

mycursor.execute("SELECT First_Name, Last_Name FROM Users WHERE Works_For = "
                 "ANY (SELECT Business_ID FROM Business WHERE Business_Type = 'Food')")

for x in mycursor:
    print(x)
