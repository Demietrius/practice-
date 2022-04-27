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

add_business(801, 'J Gilberts', 'Food', 44)



mycursor.execute('SELECT * FROM Business')

for x in mycursor:
    print(x)