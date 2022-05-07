

def handler(request):
    if "commonParams" not in request:
        return 2, " error: missing commonParams",

    if "domain" in request["commonParams"] \
        and "action" in request["commonParams"] \
        and request["commonParams"]["domain"] == "userProfile":

        if request["commonParams"] == "read":
            pass
        if request["commonParams"] == "Create":
            pass
        if request["commonParams"] == "Update":
            pass



# upserProfileApi
def create_handler(request):
    database_accessor.connect

    if "user" not in request["request"]:
        return 2, "error"
    user = database.read(requst["user"]["userID"])
    if user == None:
        database.create(request["user"])


# //seperat file
class database_accessor():

    def __init__(self):
        self.database_key = os.environ.get('DATABASE_CREDENTIALS')
        self.region = os.environ.get('REGION')
        self.host = ""
        self.user = ""
        self.password = ""
        self.database = "units"
        self.port = ""
        self.databaseConnection = None
        self.databaseCursor = None

    def create(self):
       sql = ("INSERT INTO Business (Business_ID, Business_Name, Business_Type, Number_Of_Employees)"
         "VALUES (%s, %s, %s, %s)RETurn")
       mycursor.execute(b_insert, b_data)

    def read(self, request):
        sql = "SELECT * FROM Users WHERE userId = %s"
        self.databaseCursor.yodate(sql, request)
        fetchall()
        return user

    def update(self):
        pass
