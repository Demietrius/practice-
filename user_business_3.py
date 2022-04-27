from db_access import Insert

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ng13gHc##",
    database="user_business"
)
mycursor = db.cursor()

def add_business(business_id, business_name, business_type, number_of_employees):
    b_data = (business_id, business_name, business_type, number_of_employees)
    b_insert = ("INSERT INTO Business (Business_ID, Business_Name, Business_Type, Number_Of_Employees)"
                "VALUES (%s, %s, %s, %s)")
    mycursor.execute(b_insert, b_data)

def add_user(first_name, last_name, salary, sex, user_id, works_for):
    u_data = (first_name, last_name, salary, sex, user_id, works_for)
    u_insert = ("INSERT INTO Users (First_name, Last_name, Salary, Sex, User_ID, Works_For)"
                "VALUES (%s, %s, %s, %s, %s, %s)")
    mycursor.execute(u_insert, u_data)

#add_business(801, 'J Gilberts', 'Food', 44)
#add_user('Travis', 'Barker', 3100000, 'M', 14, 501)

answer = 0
while answer != 'n':
    try:
        answer = input("Would you like to add another business? Enter Y/N: ")
        if answer.lower() == 'y':
            business_id = int(input("Enter Business ID: "))
            business_name = input("Enter Business Name: ")
            business_type = input("Enter Business Type : ")
            number_of_employees = input("Enter Number of Employees: ")
            add_business(business_id, business_name, business_type, number_of_employees)
    except:
        print('Invalid Input. Please try again.')



db.commit()

mycursor.execute('SELECT * FROM Business')
#mycursor.execute('SELECT * FROM Users')

for x in mycursor:
    print(x)