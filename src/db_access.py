import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ng13gHc##",
    database="user_business"
)
mycursor = db.cursor()

class db_connector:

    def __init__(self, business_id, business_name, busines_type, number_of_employees):
        self.host = host
        self.user = user
        self.password = password
        self.database = database



