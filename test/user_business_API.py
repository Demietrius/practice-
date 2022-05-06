from db_access import DBAccess, User, Business
import mysql.connector
import json

with open("../src/db_login.json", "r") as f:
    db_login = json.load(f)

    database = DBAccess(db_login['login']['host'],
                        db_login['login']['user'],
                        db_login['login']['password'],
                        db_login['login']['database'])


def create(request):
    if request == "add_user":
        first_name = input("Enter New User First Name: ")
        last_name = input("Enter New User Last Name: ")
        salary = input("Enter New User Salary: ")
        sex = input("Enter New User Sex: ")
        user_id = input("Enter New User ID Number: ")
        works_for = input("Enter Business ID for New User place of employment: ")
        new_user = User(first_name, last_name, salary, sex, user_id, works_for)
        User.insert_user(new_user, database)
        print(new_user.__dict__)


def update(request, database):
    if request == "update_user":
        user_id = input("Enter User ID for User you want to update: ")
        print("**********"
              "\nfirst_name"
              "\nlast_name"
              "\nsalary"
              "\nsex"
              "\nworks_for"
              "\n***********")
        attr = input("Choose an attribute you'd like to change: ")
        update = input("Enter the new attribute: ")
        db = mysql.connector.connect(
            host=database.host,
            user=database.user,
            password=database.password,
            database=database.database
        )
        mycursor = db.cursor(buffered=True)
        mycursor.execute(f"SELECT {attr} FROM Users WHERE User_ID = {user_id}")
        old_attr = mycursor.fetchall()
        mycursor.execute(f"UPDATE Users SET {attr} = {update} WHERE User_ID = {user_id}")
        db.commit()
        mycursor.execute(f"SELECT * FROM Users WHERE User_ID = {user_id}")
        return_row = mycursor.fetchall()
        print(f"You changed {attr} from {old_attr} to {update} for {user_id}")
        print(return_row)



request = input("Command List:"
                "\n **********"
                "\n add_user"
                "\n update_user"
                "\n lookup_all_users"
                "\n lookup_single_user"
                "\n lookup_self"
                "\n delete_user"
                "\n **********"
                "\nEnter command: ")

payload = {
    "commonParams":{
        "add_user": "create",
        "update_user": "update",
        "lookup_all_users": "read",
        "lookup_single_user": "read",
        "lookup_self": "read",
        "delete_user": "delete"
    }
}

if payload["commonParams"][request] == "create":
    create(request)
if payload["commonParams"][request] == "update":
    update(request, database)
