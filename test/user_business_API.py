from db_access import DBAccess, User, Business
import mysql.connector
import json




def create(request):
    first_name = request["UserInfo"]["first_name"]
    last_name = request["UserInfo"]["last_name"]
    salary = request["UserInfo"]["salary"]
    sex = request["UserInfo"]["sex"]
    works_for = request["UserInfo"]["works_for"]
    new_user = User(first_name, last_name, salary, sex, works_for)
    User.insert_user(new_user, database)
    print(new_user.__dict__)


def update(request):
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

def handler(request):
    if request["CommonParams"]["action"] == "create":
        create(request)
    if request["CommonParams"]["action"] == "update":
        update(request)
    if request["CommonParams"]["action"] == "read":
        #read(request)
        pass
    if request["CommonParams"]["action"] == "delete":
        #delete(request)
        pass

with open("../src/db_login.json", "r") as f:
    db_login = json.load(f)

    database = DBAccess(db_login['login']['host'],
                        db_login['login']['user'],
                        db_login['login']['password'],
                        db_login['login']['database'])

with open("../src/JSON_New_User.json", "r") as f:
    request = json.load(f)
    handler(request)